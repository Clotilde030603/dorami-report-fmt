from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "dorami-report-fmt" / "scripts" / "validate_skill.py"


def run_validate(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(SCRIPT), str(path)], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def copy_min_repo(tmp_path: Path) -> Path:
    dst = tmp_path / "repo"
    for rel in [
        "skills", ".agents", ".claude", "prompts", "portable", "tools", "README.md", "LICENSE", "NOTICE", ".gitignore", "install.sh", "uninstall.sh", "update.sh",
    ]:
        src = ROOT / rel
        if src.is_dir():
            shutil.copytree(src, dst / rel, ignore=shutil.ignore_patterns("__pycache__"))
        else:
            (dst / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst / rel)
    return dst


def test_validate_current_repo_passes():
    cp = run_validate(ROOT)
    assert cp.returncode == 0, cp.stderr


def test_validate_fails_when_required_skill_missing(tmp_path: Path):
    repo = copy_min_repo(tmp_path)
    (repo / "skills" / "dorami-report-fmt" / "SKILL.md").unlink()
    cp = run_validate(repo)
    assert cp.returncode != 0
    assert "missing required file" in cp.stderr


def test_validate_fails_on_public_hwpx(tmp_path: Path):
    repo = copy_min_repo(tmp_path)
    (repo / "bad.hwpx").write_bytes(b"fake")
    cp = run_validate(repo)
    assert cp.returncode != 0
    assert "public HWP/HWPX" in cp.stderr


def test_validate_fails_on_public_converted_example_dir(tmp_path: Path):
    repo = copy_min_repo(tmp_path)
    d = repo / "converted-examples"
    d.mkdir()
    (d / "example-report.md").write_text("예시 보고서\n", encoding="utf-8")
    cp = run_validate(repo)
    assert cp.returncode != 0
    assert "public forbidden directory" in cp.stderr


def test_gitignore_blocks_private_files():
    text = (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()
    assert "private/" in text
    assert "*.hwp" in text
    assert "*.hwpx" in text
