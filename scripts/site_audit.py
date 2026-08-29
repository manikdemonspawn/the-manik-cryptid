#!/usr/bin/env python3
"""Static construction audit for The Manik Cryptid Resurrection Artifact Universe."""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.refs: list[tuple[str, str]] = []
        self.anchors: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {k: v or "" for k, v in attrs}
        if tag == "a":
            self.anchors.append(values)
        for attr in ("href", "src"):
            value = values.get(attr)
            if value:
                self.refs.append((attr, value))


def is_external(value: str) -> bool:
    if value.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
        return True
    parts = urlsplit(value)
    return bool(parts.scheme or parts.netloc)


def resolve_local(source: Path, value: str) -> Path:
    path_part = urlsplit(value).path
    return (source.parent / path_part).resolve()


def load_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        return None


def audit_html(errors: list[str]) -> None:
    html_files = sorted(ROOT.rglob("*.html"))
    if not html_files:
        errors.append("No HTML files found on construction branch.")
        return

    for file in html_files:
        text = file.read_text(encoding="utf-8")
        rel = file.relative_to(ROOT)

        if 'name="robots"' not in text or "noindex" not in text:
            errors.append(f"{rel}: construction HTML is missing noindex robots metadata")

        parser = LinkParser()
        parser.feed(text)

        for attr, value in parser.refs:
            if is_external(value):
                continue
            target = resolve_local(file, value)
            if value.endswith("/"):
                target = target / "index.html"
            if not target.exists():
                errors.append(f"{rel}: broken local {attr} -> {value}")

        if rel.as_posix() == "index.html":
            root_text = text.lower()
            required_root_hrefs = {
                "realms/library/index.html",
                "realms/museum/index.html",
                "realms/krypt/index.html",
                "realms/guildhall/index.html",
                "realms/morgue/index.html",
                "realms/kurio-shop/index.html",
                "realms/forge/index.html",
                "realms/apothecary/index.html",
                "realms/katakombs/index.html",
            }
            found_root_hrefs = {value for _, value in parser.refs if value in required_root_hrefs}
            missing_root_hrefs = required_root_hrefs - found_root_hrefs
            if missing_root_hrefs:
                errors.append(f"index.html: missing active Nexus links: {sorted(missing_root_hrefs)}")

            stale_root_paths = ("realms/crypt/", "realms/catacombs/", "realms/guild-hall/", "realms/curio-shop/")
            for stale_path in stale_root_paths:
                if stale_path in root_text:
                    errors.append(f"index.html: stale active path remains: {stale_path}")

            if "katakombs-entry" not in root_text:
                errors.append("index.html: bottom Katakombs portal section is missing")
            elif root_text.find("katakombs-entry") > root_text.find("realms/katakombs/index.html"):
                errors.append("index.html: Katakombs portal is not placed inside the bottom entry section")

            if "under konstruction" not in root_text:
                errors.append("index.html: Forge/Apothecary construction marker is missing")

            for attrs in parser.anchors:
                href = attrs.get("href", "").lower()
                if "mausoleum" in href:
                    errors.append("index.html: active Mausoleum link is forbidden while creator is alive")


def audit_json(errors: list[str]) -> None:
    for file in sorted((ROOT / "data").glob("*.json")):
        load_json(file, errors)

    manifest_path = ROOT / "data" / "realm-manifest.json"
    if manifest_path.exists():
        manifest = load_json(manifest_path, errors)
        if isinstance(manifest, dict):
            nexus = manifest.get("nexus", {})
            if nexus.get("future_mausoleum_visible") is not False:
                errors.append("realm-manifest.json: future_mausoleum_visible must remain false")

            expected_realm_ids = ["library", "museum", "krypt", "guildhall", "morgue", "kurio-shop", "forge", "apothecary"]
            realms = manifest.get("realms", [])
            actual_realm_ids = [item.get("id") for item in realms]
            if actual_realm_ids != expected_realm_ids:
                errors.append(f"realm-manifest.json: primary realm order mismatch: {actual_realm_ids}")
            if len(realms) != 8:
                errors.append("realm-manifest.json: exactly eight primary realms are required")

            for item in realms:
                path = item.get("path")
                if path and not (ROOT / path).exists():
                    errors.append(f"realm-manifest.json: primary realm path does not exist: {path}")

            apothecary = next((item for item in realms if item.get("id") == "apothecary"), None)
            if not apothecary or apothecary.get("physical_parent") != "kurio-shop" or apothecary.get("status") != "under-konstruction":
                errors.append("realm-manifest.json: Apothecary must be upstairs in Kurio Shop and under-konstruction")

            forge = next((item for item in realms if item.get("id") == "forge"), None)
            if not forge or forge.get("status") != "under-konstruction":
                errors.append("realm-manifest.json: Forge must remain an under-konstruction primary realm")

            subrealms = manifest.get("subrealms", [])
            forbidden = next((item for item in subrealms if item.get("id") == "forbidden-library"), None)
            if not forbidden or forbidden.get("parent_id") != "library":
                errors.append("realm-manifest.json: Forbidden Library must remain inside Library")

            infrastructure = manifest.get("infrastructure", [])
            katakombs = next((item for item in infrastructure if item.get("id") == "katakombs"), None)
            if not katakombs or katakombs.get("public_nexus_portal") is not True or katakombs.get("nexus_position") != "bottom-infrastructure":
                errors.append("realm-manifest.json: Katakombs must be a bottom Nexus infrastructure portal")

            future = manifest.get("future", [])
            mausoleum = next((item for item in future if item.get("id") == "mausoleum"), None)
            if not mausoleum or mausoleum.get("posthumous_only") is not True or mausoleum.get("active") is not False:
                errors.append("realm-manifest.json: Mausoleum must remain inactive and posthumous-only")


def audit_artifacts(errors: list[str]) -> None:
    path = ROOT / "data" / "artifacts.json"
    if not path.exists():
        errors.append("data/artifacts.json: Kanonikal artifact registry missing")
        return

    payload = load_json(path, errors)
    if not isinstance(payload, dict):
        return

    seen: set[str] = set()
    for item in payload.get("artifacts", []):
        artifact_id = item.get("artifact_id")
        if not artifact_id:
            errors.append("artifacts.json: artifact without artifact_id")
            continue
        if artifact_id in seen:
            errors.append(f"artifacts.json: duplicate artifact_id {artifact_id!r}")
        seen.add(artifact_id)

        media = item.get("media") or {}
        hero = media.get("hero_image")
        if hero:
            candidate = (ROOT / hero.lstrip("/")).resolve()
            if not candidate.exists():
                errors.append(f"artifacts.json: {artifact_id} hero_image does not exist: {hero}")

        for platform in item.get("platforms", []):
            url = (platform or {}).get("url")
            if url and urlsplit(url).scheme not in {"http", "https"}:
                errors.append(f"artifacts.json: {artifact_id} platform URL must be http/https: {url}")


def audit_visual_targets(errors: list[str]) -> None:
    path = ROOT / "data" / "visual-targets.json"
    if not path.exists():
        errors.append("data/visual-targets.json: visual target manifest missing")
        return

    payload = load_json(path, errors)
    if not isinstance(payload, dict):
        return

    ids = {item.get("id") for item in payload.get("targets", [])}
    required = {
        "nexus-master", "museum-master", "library-master", "forbidden-library-master",
        "morgue-master", "krypt-master", "guildhall-master", "kurio-shop-master",
        "forge-master", "apothecary-master", "yard-sale-master", "katakombs-master"
    }
    missing = required - ids
    if missing:
        errors.append(f"visual-targets.json: missing target IDs: {sorted(missing)}")

    stale_ids = {"crypt-master", "guild-hall-master", "curio-shop-master", "catacombs-master"}
    stale_present = stale_ids & ids
    if stale_present:
        errors.append(f"visual-targets.json: stale target IDs remain: {sorted(stale_present)}")

    posthumous = payload.get("posthumous", [])
    mausoleum = next((item for item in posthumous if item.get("id") == "mausoleum-master"), None)
    if not mausoleum or mausoleum.get("status") != "inactive-posthumous-only":
        errors.append("visual-targets.json: Mausoleum target must remain inactive-posthumous-only")


def audit_forbidden_library(errors: list[str]) -> None:
    gate = ROOT / "realms" / "library" / "forbidden" / "index.html"
    if not gate.exists():
        errors.append("Forbidden Library gate page missing")
        return

    text = gate.read_text(encoding="utf-8").lower()
    required = ["no adult content loaded", "real age", "restricted"]
    for phrase in required:
        if phrase not in text:
            errors.append(f"Forbidden Library gate missing construction safety marker: {phrase!r}")


def audit_museum_keeper_artifact(errors: list[str]) -> None:
    museum = ROOT / "realms" / "museum" / "index.html"
    if not museum.exists():
        errors.append("Museum page missing")
        return

    text = museum.read_text(encoding="utf-8")
    required = [
        "RAU-EFI-2026-0828-001",
        "Sertifikate of Ecosystem-First Inquiry",
        "KANON Keeper Edition",
        "Permanent Museum wall artifact",
    ]
    for phrase in required:
        if phrase not in text:
            errors.append(f"Museum keeper Sertifikate missing required marker: {phrase!r}")


def audit_active_naming(errors: list[str]) -> None:
    """Catch stale architecture in active source while allowing retired path notices."""
    excluded = {"realms/crypt", "realms/catacombs", "realms/guild-hall", "realms/curio-shop"}
    files = [ROOT / "README.md", ROOT / "index.html", ROOT / "realm-index.html"]
    files += sorted((ROOT / "docs").glob("*.md"))
    files += sorted((ROOT / "data").glob("*.json"))
    files += sorted((ROOT / "templates").glob("*.html"))
    files += sorted((ROOT / "realms").rglob("*.html"))

    stale_terms = {
        "The Crypt": "The Krypt",
        "The Catacombs": "The Katakombs",
        "The Curio Shop": "The Kurio Shop",
        "The Guild Hall": "The Guildhall",
    }
    for file in files:
        rel = file.relative_to(ROOT).as_posix()
        if any(rel == path or rel.startswith(path + "/") for path in excluded):
            continue
        text = file.read_text(encoding="utf-8")
        for stale, current in stale_terms.items():
            if re.search(rf"\b{re.escape(stale)}\b", text, flags=re.IGNORECASE):
                errors.append(f"{rel}: stale active naming {stale!r}; use {current!r}")


def main() -> int:
    errors: list[str] = []
    audit_html(errors)
    audit_json(errors)
    audit_artifacts(errors)
    audit_visual_targets(errors)
    audit_forbidden_library(errors)
    audit_museum_keeper_artifact(errors)
    audit_active_naming(errors)

    if errors:
        print("CONSTRUCTION AUDIT FAILED\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("CONSTRUCTION AUDIT PASSED")
    print("- local HTML references resolve")
    print("- construction pages remain noindex")
    print("- JSON data files parse")
    print("- artifact IDs/media/platform URLs validate")
    print("- primary realm order, bottom Katakombs portal, and naming locks validate")
    print("- visual-target manifest is complete")
    print("- living-site Mausoleum remains inactive")
    print("- Forbidden Library retains construction safety markers")
    return 0


if __name__ == "__main__":
    sys.exit(main())
