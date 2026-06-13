#!/usr/bin/env bash
set -euo pipefail
usage(){ echo "Usage: $0 --codex | --claude | --all"; }
remove_skill(){
  local dest="$1"
  if [ -d "$dest" ]; then
    rm -rf "$dest"
    echo "removed: $dest"
  else
    echo "not installed: $dest"
  fi
}
[ $# -eq 1 ] || { usage; exit 2; }
case "$1" in
  --codex) remove_skill "$HOME/.agents/skills/dorami-report-fmt" ;;
  --claude) remove_skill "$HOME/.claude/skills/dorami-report-fmt" ;;
  --all) remove_skill "$HOME/.agents/skills/dorami-report-fmt"; remove_skill "$HOME/.claude/skills/dorami-report-fmt" ;;
  *) usage; exit 2 ;;
esac
