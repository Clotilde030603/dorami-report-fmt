#!/usr/bin/env python3
"""Validate dorami-report-fmt public repository structure."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_FILES = [
    "skills/dorami-report-fmt/SKILL.md",
    "skills/dorami-report-fmt/references/style-guide.md",
    "skills/dorami-report-fmt/references/do-not.md",
    "skills/dorami-report-fmt/references/report-template.md",
    "skills/dorami-report-fmt/references/ai-like-phrasing-guide.md",
    "skills/dorami-report-fmt/references/local-reference-guide.md",
    "skills/dorami-report-fmt/references/benchmark-guide.md",
    "skills/dorami-report-fmt/references/style-extraction-loop.md",
    ".agents/skills/dorami-report-fmt/SKILL.md",
    ".claude/skills/dorami-report-fmt/SKILL.md",
    "prompts/README.md",
    "prompts/dorami-report-fmt-system-prompt.md",
    "prompts/dorami-report-fmt-user-prompt.md",
    "prompts/dorami-report-fmt-short.md",
    "portable/dorami-report-fmt.md",
    "README.md",
    "LICENSE",
    "NOTICE",
    ".gitignore",
    "install.sh",
    "uninstall.sh",
    "update.sh",
    "tools/convert_hwp_to_markdown.py",
    "tools/prepare_private_references.py",
    "tools/import_im_not_ai_patterns.py",
    "tools/extract_style_from_private_refs.py",
]

README_REQUIRED = [
    "dorami-report-fmt란?",
    "주요 기능",
    "하지 않는 일",
    "설치",
    "Gajae Code 및 기타 AI에서 사용",
    "사용 예시",
    "내부 처리 흐름",
    "im-not-ai와의 관계",
    "저장소 구조",
    "개발 문서",
    "검증",
]

GITIGNORE_REQUIRED = ["private/", "*.hwp", "*.hwpx"]
PUBLIC_FORBIDDEN_DIRS = {"local-references", "converted-examples", "redacted-examples", "raw", "tmp"}
SUSPICIOUS_REPORT_NAME = re.compile(r"(converted|redacted|sample|example|actual|real|예시|사례|원본).*(report|보고서)|(?:보고서).*(?:예시|사례|원본)", re.I)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    root = root.resolve()

    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            errors.append(f"missing required file: {rel}")

    skill = root / "skills/dorami-report-fmt/SKILL.md"
    if skill.is_file():
        text = read(skill)
        if not text.startswith("---\n") or "\n---\n" not in text[4:]:
            errors.append("SKILL.md missing YAML frontmatter")
        front = text.split("---", 2)[1] if text.startswith("---") else ""
        if not re.search(r"^name:\s*dorami-report-fmt\s*$", front, re.M):
            errors.append("SKILL.md frontmatter name must be dorami-report-fmt")
        if not re.search(r"^description:\s*.+", front, re.M):
            errors.append("SKILL.md frontmatter description is missing")
        for rel in [".agents/skills/dorami-report-fmt/SKILL.md", ".claude/skills/dorami-report-fmt/SKILL.md"]:
            p = root / rel
            if p.is_file() and p.read_text(encoding="utf-8") != text:
                errors.append(f"entrypoint not synchronized with source: {rel}")

    readme = root / "README.md"
    if readme.is_file():
        r = read(readme)
        for marker in README_REQUIRED:
            if marker not in r:
                errors.append(f"README missing section: {marker}")
        forbidden_readme = ["AI " + "탐지 " + "회피", "AI detector " + "bypass", "탐지 " + "회피"]
        for term in forbidden_readme:
            if term in r:
                errors.append(f"README contains forbidden purpose wording: {term}")

    gitignore = root / ".gitignore"
    if gitignore.is_file():
        g = read(gitignore)
        for item in GITIGNORE_REQUIRED:
            if item not in g.splitlines():
                errors.append(f".gitignore missing: {item}")

    for p in root.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(root)
        parts = set(rel.parts)
        if ".git" in parts or ".omx" in parts or "private" in parts or "__pycache__" in parts:
            continue
        if p.suffix.lower() in {".hwp", ".hwpx"}:
            errors.append(f"public HWP/HWPX file found: {rel.as_posix()}")
        if parts & PUBLIC_FORBIDDEN_DIRS:
            errors.append(f"public forbidden directory contains file: {rel.as_posix()}")
        if p.suffix.lower() == ".md" and SUSPICIOUS_REPORT_NAME.search(p.name) and not rel.as_posix().startswith(("skills/", "prompts/", "portable/")):
            errors.append(f"possible public converted example report: {rel.as_posix()}")

    return errors


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Validate dorami-report-fmt repository structure.")
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args(argv)
    errors = validate(Path(args.root))
    if errors:
        print("Skill validation failed:", file=sys.stderr)
        for e in errors:
            print(f"- {e}", file=sys.stderr)
        return 1
    print("Skill validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
