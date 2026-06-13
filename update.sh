#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$ROOT/skills/dorami-report-fmt"
copy_if_exists(){
  local dest="$1"
  if [ -d "$dest" ]; then
    rm -rf "$dest"
    mkdir -p "$dest"
    tar -C "$SRC" --exclude='private' -cf - . | tar -C "$dest" -xf -
    echo "updated: $dest"
  fi
}
copy_if_exists "$HOME/.agents/skills/dorami-report-fmt"
copy_if_exists "$HOME/.claude/skills/dorami-report-fmt"
echo "update complete. private/ was not copied."
