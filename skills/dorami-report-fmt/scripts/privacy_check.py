#!/usr/bin/env python3
"""Privacy and public-package safety scanner for dorami-report-fmt."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

TEXT_SUFFIXES = {".md", ".txt", ".rst", ".csv", ".json", ".yml", ".yaml", ".toml", ".sh", ".py"}
DEFAULT_EXCLUDE_DIRS = {".git", ".omx", "__pycache__", ".pytest_cache", "node_modules", "private"}
ALWAYS_EXCLUDE_DIRS = {".git", ".omx", "__pycache__", ".pytest_cache", "node_modules"}
PUBLIC_FORBIDDEN_DIRS = {"local-references", "converted-examples", "redacted-examples", "raw", "tmp"}

PATTERNS = [
    ("email", re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")),
    ("korean_mobile", re.compile(r"\b01[016789][- .]?\d{3,4}[- .]?\d{4}\b")),
    ("resident_registration_like", re.compile(r"\b\d{6}[- ]?[1-4]\d{6}\b")),
    ("birth_date_like", re.compile(r"\b(?:19|20)\d{2}[.\-/년 ]\s?(?:0?[1-9]|1[0-2])[.\-/월 ]\s?(?:0?[1-9]|[12]\d|3[01])(?:일)?\b")),
    ("student_id_like", re.compile(r"(?:학번|student\s*id)\s*[:：]\s*[A-Za-z0-9-]{4,}", re.I)),
    ("field_name_value", re.compile(r"(?:성명|학교명|이메일|휴대폰|전화번호|생년월일)\s*[:：]\s*[^\s\[\]\n]{2,}")),
    ("account_number_like", re.compile(r"(?:계좌번호|account)\s*[:：]\s*[0-9-]{8,}")),
]

SUSPICIOUS_REPORT_NAME = re.compile(r"(converted|redacted|sample|example|actual|real|report|보고서|예시|사례|원본)", re.I)


def is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def iter_files(root: Path, include_private: bool):
    exclude = set(ALWAYS_EXCLUDE_DIRS)
    if not include_private:
        exclude.add("private")
    for p in root.rglob("*"):
        if any(part in exclude for part in p.parts):
            continue
        if p.is_file():
            yield p


def scan(root: Path, include_private: bool = False) -> list[str]:
    findings: list[str] = []
    root = root.resolve()
    for path in iter_files(root, include_private):
        rel = path.relative_to(root)
        rel_s = rel.as_posix()
        parts = set(rel.parts)
        in_private = "private" in parts
        if not in_private and path.suffix.lower() in {".hwp", ".hwpx"}:
            findings.append(f"FORBIDDEN_HWP_PUBLIC: {rel_s}")
        if not in_private and parts & PUBLIC_FORBIDDEN_DIRS:
            findings.append(f"FORBIDDEN_PUBLIC_DIRECTORY: {rel_s}")
        if not in_private and path.suffix.lower() == ".md":
            lowered = rel_s.lower()
            allow = {
                "README.md", "AGENTS.md", "NOTICE",
                "skills/dorami-report-fmt/references/report-template.md",
            }
            if rel_s not in allow and SUSPICIOUS_REPORT_NAME.search(path.name) and not rel_s.startswith(("skills/", "prompts/", "portable/")):
                findings.append(f"POSSIBLE_REPORT_EXAMPLE: {rel_s}")
        if path.suffix.lower() in TEXT_SUFFIXES:
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                try:
                    text = path.read_text(encoding="utf-8", errors="ignore")
                except OSError:
                    continue
            for name, pattern in PATTERNS:
                for match in pattern.finditer(text):
                    snippet = match.group(0).replace("\n", " ")[:80]
                    findings.append(f"{name}: {rel_s}: {snippet}")
    return findings


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Scan public package files for private data and unsafe examples.")
    parser.add_argument("path", nargs="?", default=".", help="Path to scan")
    parser.add_argument("--include-private", action="store_true", help="Also scan private/ local-only files")
    args = parser.parse_args(argv)
    root = Path(args.path)
    findings = scan(root, include_private=args.include_private)
    if findings:
        print("Privacy/public-safety check failed:", file=sys.stderr)
        for item in findings:
            print(f"- {item}", file=sys.stderr)
        return 1
    print("Privacy/public-safety check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
