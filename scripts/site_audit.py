#!/usr/bin/env python3
"""Static construction audit for The Manik Cryptid Resurrection Artifact Universe."""

from __future__ import annotations

import json
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

            future = manifest.get("future", [])
            mausoleum = next((item for item in future if item.get("id") == "mausoleum"), None)
            if not mausoleum or mausoleum.get("posthumous_only") is not True or mausoleum.get("active") is not False:
                errors.append("realm-manifest.json: Mausoleum must remain inactive and posthumous-only")


def audit_artifacts(errors: list[str]) -> None:
    path = ROOT / "data" / "artifacts.json"
    if not path.exists():
        errors.append("data/artifacts.json: canonical artifact registry missing")
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
        "morgue-master", "crypt-master", "guild-hall-master", "curio-shop-master",
        "apothecary-master", "yard-sale-master", "catacombs-master"
    }
    missing = required - ids
    if missing:
        errors.append(f"visual-targets.json: missing target IDs: {sorted(missing)}")

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


def main() -> int:
    errors: list[str] = []
    audit_html(errors)
    audit_json(errors)
    audit_artifacts(errors)
    audit_visual_targets(errors)
    audit_forbidden_library(errors)

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
    print("- visual-target manifest is complete")
    print("- living-site Mausoleum remains inactive")
    print("- Forbidden Library retains construction safety markers")
    return 0


if __name__ == "__main__":
    sys.exit(main())
