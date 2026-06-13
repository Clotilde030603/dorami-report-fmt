#!/usr/bin/env python3
"""Convert local-only HWP/HWPX source files into private/converted Markdown.

This tool never writes into public skill folders. It is intentionally conservative:
if content cannot be extracted, it records notes instead of guessing.
"""
from __future__ import annotations

import argparse
import html
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PRIVATE = ROOT / "private"
DEFAULT_SOURCE = PRIVATE / "source"
DEFAULT_OUT = PRIVATE / "converted"
NOTES = PRIVATE / "conversion-notes.md"


def safe_output_path(source: Path, out_dir: Path) -> Path:
    name = source.stem.replace("/", "_").replace("\\", "_") + ".md"
    target = (out_dir / name).resolve()
    if not str(target).startswith(str((PRIVATE / "converted").resolve())):
        raise RuntimeError("Refusing to write outside private/converted")
    return target


def write_note(message: str) -> None:
    PRIVATE.mkdir(exist_ok=True)
    with NOTES.open("a", encoding="utf-8") as f:
        f.write(message.rstrip() + "\n")


def xml_text_from_hwpx(path: Path) -> str:
    chunks: list[str] = []
    with zipfile.ZipFile(path) as zf:
        names = [n for n in zf.namelist() if n.lower().endswith(".xml")]
        preferred = sorted([n for n in names if "section" in n.lower() or "contents/" in n.lower()]) or sorted(names)
        for name in preferred:
            try:
                data = zf.read(name)
                root = ET.fromstring(data)
            except Exception:
                continue
            texts: list[str] = []
            for elem in root.iter():
                tag = elem.tag.split("}")[-1].lower()
                if tag in {"t", "text"} and elem.text:
                    texts.append(elem.text)
                elif elem.text and tag.endswith("t"):
                    texts.append(elem.text)
            if texts:
                chunks.append(" ".join(t.strip() for t in texts if t.strip()))
    return "\n\n".join(chunks).strip()


def run_tool(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)


def convert_hwp_with_tools(path: Path) -> tuple[str, str | None]:
    hwp5txt = shutil.which("hwp5txt")
    if hwp5txt:
        cp = run_tool([hwp5txt, str(path)])
        if cp.returncode == 0 and cp.stdout.strip():
            return cp.stdout.strip(), None
        return "", f"hwp5txt failed for {path.name}: {cp.stderr.strip() or cp.stdout.strip()}"

    hwp5html = shutil.which("hwp5html")
    if hwp5html:
        with tempfile.TemporaryDirectory() as td:
            cp = run_tool([hwp5html, str(path)], cwd=Path(td))
            if cp.returncode == 0:
                html_files = list(Path(td).rglob("*.html"))
                if html_files:
                    raw = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in html_files)
                    text = re_html_to_text(raw)
                    if text.strip():
                        return text.strip(), None
            return "", f"hwp5html failed for {path.name}: {cp.stderr.strip() or cp.stdout.strip()}"

    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    pandoc = shutil.which("pandoc")
    if soffice:
        with tempfile.TemporaryDirectory() as td:
            out = Path(td)
            cp = run_tool([soffice, "--headless", "--convert-to", "txt", "--outdir", str(out), str(path)])
            txts = list(out.glob("*.txt"))
            if cp.returncode == 0 and txts:
                return txts[0].read_text(encoding="utf-8", errors="ignore").strip(), None
            if pandoc:
                cp2 = run_tool([soffice, "--headless", "--convert-to", "docx", "--outdir", str(out), str(path)])
                docxs = list(out.glob("*.docx"))
                if cp2.returncode == 0 and docxs:
                    cp3 = run_tool([pandoc, str(docxs[0]), "-t", "markdown"])
                    if cp3.returncode == 0 and cp3.stdout.strip():
                        return cp3.stdout.strip(), None
            return "", f"LibreOffice conversion failed for {path.name}: {cp.stderr.strip() or cp.stdout.strip()}"

    return "", "No supported HWP converter found. Install pyhwp/hwp5txt, LibreOffice, or convert the file to DOCX/PDF/TXT/HTML and place it in private/source."


def re_html_to_text(raw: str) -> str:
    import re
    text = re.sub(r"<br\s*/?>", "\n", raw, flags=re.I)
    text = re.sub(r"</p>", "\n\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    return re.sub(r"[ \t]+", " ", text)


def markdown_from_text(title: str, text: str) -> str:
    text = "\n".join(line.rstrip() for line in text.splitlines())
    return f"# {title}\n\n{text.strip()}\n"


def convert_file(path: Path, out_dir: Path) -> bool:
    out_dir.mkdir(parents=True, exist_ok=True)
    suffix = path.suffix.lower()
    text = ""
    error = None
    if suffix == ".hwpx":
        try:
            text = xml_text_from_hwpx(path)
            if not text:
                error = "HWPX XML text extraction produced no text."
        except Exception as exc:
            error = f"HWPX extraction failed: {exc}"
    elif suffix == ".hwp":
        text, error = convert_hwp_with_tools(path)
    elif suffix in {".txt", ".md"}:
        text = path.read_text(encoding="utf-8", errors="ignore")
    else:
        error = f"Unsupported file type: {suffix}. Convert to HWPX, DOCX/PDF/TXT/HTML manually, or add a converter."

    if text.strip():
        target = safe_output_path(path, out_dir)
        target.write_text(markdown_from_text(path.stem, text), encoding="utf-8")
        print(f"converted: {path} -> {target}")
        return True
    write_note(f"- {path.name}: {error or 'No text extracted.'}")
    print(f"failed: {path.name}; see {NOTES}", file=sys.stderr)
    return False


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Convert private/source HWP/HWPX files to private/converted Markdown.")
    parser.add_argument("source", nargs="?", default=str(DEFAULT_SOURCE), help="Source directory under private/source")
    args = parser.parse_args(argv)
    source = Path(args.source).resolve()
    out_dir = DEFAULT_OUT.resolve()
    if not str(source).startswith(str(PRIVATE.resolve())):
        print("Refusing to read outside private/. Put files under private/source/.", file=sys.stderr)
        return 2
    source.mkdir(parents=True, exist_ok=True)
    files = [p for p in source.rglob("*") if p.is_file() and p.suffix.lower() in {".hwp", ".hwpx", ".txt", ".md"}]
    if not files:
        print("No supported files found in private/source/.")
        return 0
    ok = 0
    for p in files:
        ok += int(convert_file(p, out_dir))
    print("Reminder: private/converted is local-only. Do not commit converted files to GitHub.")
    return 0 if ok == len(files) else 1


if __name__ == "__main__":
    raise SystemExit(main())
