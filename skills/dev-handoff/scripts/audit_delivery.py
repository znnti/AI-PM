#!/usr/bin/env python3
"""Audit a product prototype package before developer handoff."""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ARCHIVE_PARTS = {"archive", "archived", ".archive"}
CANONICAL_DOCS = ("PRD.md", "Interaction-Spec.md", "Design.md", "Asset-Spec.md")
HANDOFF_NAMES = ("Docs-Handoff.md",)


def is_archived(path: Path) -> bool:
    lower_parts = {part.lower() for part in path.parts}
    return bool(lower_parts & ARCHIVE_PARTS) or ".archive." in path.name.lower()


class PrototypeParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.refs: list[str] = []

    def handle_starttag(self, _tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.append(str(values["id"]))
        for key in ("src", "href", "poster"):
            if values.get(key):
                self.refs.append(str(values[key]))


def active_matches(root: Path, name: str) -> list[Path]:
    return [path for path in root.rglob(name) if path.is_file() and not is_archived(path)]


def local_ref_path(html: Path, ref: str) -> Path | None:
    parsed = urlparse(ref)
    if parsed.scheme or ref.startswith(("#", "//", "data:", "javascript:", "mailto:")):
        return None
    clean = unquote(parsed.path)
    if not clean:
        return None
    return (html.parent / clean).resolve()


def audit(root: Path) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []
    info: list[str] = []

    for name in CANONICAL_DOCS:
        matches = active_matches(root, name)
        if not matches:
            warnings.append(f"Missing canonical document: {name}")
        elif len(matches) > 1:
            warnings.append(
                f"Multiple active {name} files: " + ", ".join(str(p.relative_to(root)) for p in matches)
            )

    handoffs = [path for name in HANDOFF_NAMES for path in active_matches(root, name)]
    if not handoffs:
        warnings.append("Missing canonical handoff entry: Docs-Handoff.md")
    elif len(handoffs) > 1:
        warnings.append(
            "Multiple active handoff entries: "
            + ", ".join(str(path.relative_to(root)) for path in handoffs)
        )

    html_files = [path for path in root.rglob("*.html") if path.is_file() and not is_archived(path)]
    if not html_files:
        errors.append("No active HTML prototype found")

    for html in html_files:
        parser = PrototypeParser()
        try:
            parser.feed(html.read_text(encoding="utf-8", errors="replace"))
        except OSError as exc:
            errors.append(f"Cannot read {html.relative_to(root)}: {exc}")
            continue
        duplicates = sorted(key for key, count in Counter(parser.ids).items() if count > 1)
        if duplicates:
            errors.append(f"Duplicate IDs in {html.relative_to(root)}: {', '.join(duplicates)}")
        for ref in parser.refs:
            target = local_ref_path(html, ref)
            if target is not None and not target.exists():
                errors.append(f"Broken local reference in {html.relative_to(root)}: {ref}")

    info.append(f"Audited {len(html_files)} HTML file(s)")
    return {"root": str(root), "errors": errors, "warnings": warnings, "info": info}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_root", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    root = args.project_root.expanduser().resolve()
    if not root.is_dir():
        parser.error(f"project root is not a directory: {root}")
    result = audit(root)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        for label in ("errors", "warnings", "info"):
            for item in result[label]:
                print(f"{label[:-1].upper()}: {item}")
    sys.exit(1 if result["errors"] else 0)


if __name__ == "__main__":
    main()
