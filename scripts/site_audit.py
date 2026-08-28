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
    candidate = (source.parent / path_part).resolve()
    return candidate


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
        try:
            json.loads(file.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{file.relative_to(ROOT)}: invalid JSON: {exc}")

    manifest_path = ROOT / "data" / "realm-manifest.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        nexus = manifest.get("nexus", {})
        if nexus.get("future_mausoleum_visible") is not False:
            errors.append("realm-manifest.json: future_mausoleum_visible must remain false")

        future = manifest.get("future", [])
        mausoleum = next((item for item in future if item.get("id") == "mausoleum"), None)
        if not mausoleum or mausoleum.get("posthumous_only") is not True or mausoleum.get("active") is not False:
            errors.append("realm-manifest.json: Mausoleum must remain inactive and posthumous-only")


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
    print("- living-site Mausoleum remains inactive")
    print("- Forbidden Library retains construction safety markers")
    return 0


if __name__ == "__main__":
    sys.exit(main())
