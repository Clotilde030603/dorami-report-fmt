#!/usr/bin/env python3
"""Synchronize Codex and Claude Code project skill entrypoints with the canonical skill."""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "skills" / "dorami-report-fmt" / "SKILL.md"
TARGETS = [
    ROOT / ".agents" / "skills" / "dorami-report-fmt" / "SKILL.md",
    ROOT / ".claude" / "skills" / "dorami-report-fmt" / "SKILL.md",
]


def main() -> int:
    if not SOURCE.is_file():
        print(f"Missing source skill: {SOURCE}")
        return 1
    for target in TARGETS:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(SOURCE, target)
        print(f"synced: {target.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
