from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "dorami-report-fmt" / "scripts" / "privacy_check.py"


def run_privacy(path: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(SCRIPT), str(path), *args], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def test_privacy_check_fails_on_email(tmp_path: Path):
    (tmp_path / "README.md").write_text("담당자: " + "user" + "@" + "example.com" + "\n", encoding="utf-8")
    cp = run_privacy(tmp_path)
    assert cp.returncode != 0
    assert "email" in cp.stderr


def test_privacy_check_passes_safe_file(tmp_path: Path):
    (tmp_path / "README.md").write_text("공개 가능한 문체 가이드입니다.\n", encoding="utf-8")
    cp = run_privacy(tmp_path)
    assert cp.returncode == 0, cp.stderr


def test_privacy_check_fails_on_public_hwp(tmp_path: Path):
    (tmp_path / "sample.hwp").write_bytes(b"fake")
    cp = run_privacy(tmp_path)
    assert cp.returncode != 0
    assert "FORBIDDEN_HWP_PUBLIC" in cp.stderr


def test_privacy_check_excludes_private_by_default(tmp_path: Path):
    p = tmp_path / "private"
    p.mkdir()
    (p / "secret.md").write_text("user" + "@" + "example.com" + "\n", encoding="utf-8")
    cp = run_privacy(tmp_path)
    assert cp.returncode == 0, cp.stderr
    cp2 = run_privacy(tmp_path, "--include-private")
    assert cp2.returncode != 0
