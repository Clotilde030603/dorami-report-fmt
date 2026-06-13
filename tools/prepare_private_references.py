#!/usr/bin/env python3
"""Redact local converted Markdown into private/redacted for local-only style reference."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRIVATE = ROOT / "private"
DEFAULT_IN = PRIVATE / "converted"
DEFAULT_OUT = PRIVATE / "redacted"

REPLACEMENTS = [
    (re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"), "[이메일]"),
    (re.compile(r"\b01[016789][- .]?\d{3,4}[- .]?\d{4}\b"), "[전화번호]"),
    (re.compile(r"\b\d{6}[- ]?[1-4]\d{6}\b"), "[식별정보]"),
    (re.compile(r"\b(?:19|20)\d{2}[.\-/년 ]\s?(?:0?[1-9]|1[0-2])[.\-/월 ]\s?(?:0?[1-9]|[12]\d|3[01])(?:일)?\b"), "[생년월일]"),
    (re.compile(r"(성명|이름)\s*[:：]\s*[^\n]+"), r"\1: [이름]"),
    (re.compile(r"학교명\s*[:：]\s*[^\n]+"), "학교명: [학교명]"),
    (re.compile(r"전공명?\s*[:：]\s*[^\n]+"), "전공: [전공명]"),
    (re.compile(r"학번\s*[:：]\s*[^\n]+"), "학번: [식별정보]"),
    (re.compile(r"(팀명|팀\s*이름)\s*[:：]\s*[^\n]+"), r"\1: [팀명]"),
    (re.compile(r"(멘토|지도교수)\s*[:：]\s*[^\n]+"), r"\1: [멘토1]"),
    (re.compile(r"계좌번호\s*[:：]\s*[0-9-]+"), "계좌번호: [식별정보]"),
]

COMMON_SCHOOL = re.compile(r"[가-힣A-Za-z0-9]+(?:대학교|대학|고등학교|중학교)")
COMMON_DEPT = re.compile(r"[가-힣A-Za-z0-9]+(?:학과|전공|학부)")
SAFE_PLACEHOLDERS = {"[이름]", "[팀원1]", "[팀원2]", "[멘토1]", "[학교명]", "[전공명]", "[이메일]", "[전화번호]", "[생년월일]", "[식별정보]", "[팀명]"}
BRACKETED_LABEL = re.compile(r"\[[^\]\n]{2,30}\]")


def _redact_bracketed(match: re.Match[str]) -> str:
    value = match.group(0)
    return value if value in SAFE_PLACEHOLDERS else "[팀명]"


def redact(text: str) -> str:
    for pat, repl in REPLACEMENTS:
        text = pat.sub(repl, text)
    text = COMMON_SCHOOL.sub("[학교명]", text)
    text = COMMON_DEPT.sub("[전공명]", text)
    text = BRACKETED_LABEL.sub(_redact_bracketed, text)
    return text


def safe_redacted_name(path: Path) -> str:
    stem = redact(path.stem)
    stem = re.sub(r"[^0-9A-Za-z가-힣._ ()\[\]-]+", "_", stem).strip("._ ") or "redacted"
    return stem + path.suffix


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Redact private converted Markdown files for local-only references.")
    parser.add_argument("source", nargs="?", default=str(DEFAULT_IN), help="Source directory under private/converted")
    args = parser.parse_args(argv)
    source = Path(args.source).resolve()
    if not str(source).startswith(str(PRIVATE.resolve())):
        print("Refusing to read outside private/.", file=sys.stderr)
        return 2
    DEFAULT_OUT.mkdir(parents=True, exist_ok=True)
    count = 0
    for path in source.rglob("*.md"):
        rel = path.relative_to(source)
        target = DEFAULT_OUT / rel.parent / safe_redacted_name(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(redact(path.read_text(encoding="utf-8", errors="ignore")), encoding="utf-8")
        print(f"redacted: {path} -> {target}")
        count += 1
    print("경고: private/converted 및 private/redacted 파일은 로컬 참고용입니다. GitHub에 커밋하지 마세요.")
    return 0 if count else 0


if __name__ == "__main__":
    raise SystemExit(main())
