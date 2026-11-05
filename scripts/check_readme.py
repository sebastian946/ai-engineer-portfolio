#!/usr/bin/env python3
"""Check that a project README contains every mandatory section.

Usage:
    python scripts/check_readme.py [README_PATH ...]

Defaults to templates/PROJECT_README.md when no path is given.
Exits with code 1 and lists the missing sections if any README is incomplete,
otherwise exits with code 0.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_SECTIONS: list[str] = [
    "Problem",
    "Architecture",
    "Evaluation",
    "Cost & latency",
    "Trade-offs & decisions",
    "Run it",
    "Limitations & next steps",
]

DEFAULT_README = Path("templates/PROJECT_README.md")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$")


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def extract_headings(markdown: str) -> list[str]:
    """Return the normalized text of every ATX heading, skipping fenced code."""
    headings: list[str] = []
    in_fence = False
    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped.startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = HEADING_RE.match(stripped)
        if match:
            headings.append(_normalize(match.group(1)))
    return headings


def missing_sections(markdown: str) -> list[str]:
    headings = set(extract_headings(markdown))
    return [s for s in REQUIRED_SECTIONS if _normalize(s) not in headings]


def check_file(path: Path) -> list[str]:
    if not path.is_file():
        return [f"<file not found: {path}>"]
    return missing_sections(path.read_text(encoding="utf-8"))


def main(argv: list[str]) -> int:
    paths = [Path(p) for p in argv] or [DEFAULT_README]
    failed = False
    for path in paths:
        missing = check_file(path)
        if missing:
            failed = True
            print(f"FAIL {path}: missing {len(missing)} required section(s):")
            for section in missing:
                print(f"  - {section}")
        else:
            print(f"OK   {path}: all {len(REQUIRED_SECTIONS)} required sections present")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
