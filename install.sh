#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$ROOT/skills/dorami-report-fmt"
usage(){ echo "Usage: $0 --codex | --claude | --all"; }
copy_skill(){
  local dest="$1"
  mkdir -p "$(dirname "$dest")"
  rm -rf "$dest"
  mkdir -p "$dest"
  tar -C "$SRC" --exclude='private' -cf - . | tar -C "$dest" -xf -
  echo "installed: $dest"
}
[ $# -eq 1 ] || { usage; exit 2; }
case "$1" in
  --codex) copy_skill "$HOME/.agents/skills/dorami-report-fmt" ;;
  --claude) copy_skill "$HOME/.claude/skills/dorami-report-fmt" ;;
  --all) copy_skill "$HOME/.agents/skills/dorami-report-fmt"; copy_skill "$HOME/.claude/skills/dorami-report-fmt" ;;
  *) usage; exit 2 ;;
esac
cat <<'MSG'

사용 예시:
- 이 초안을 dorami-report-fmt 스킬로 다듬어줘.
- 도라미 보고서체로 보고서 문체를 정리해줘.

주의: private/ 폴더와 개인 보고서 자료는 설치 대상이 아닙니다.
MSG
