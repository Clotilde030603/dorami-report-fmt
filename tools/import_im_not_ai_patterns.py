#!/usr/bin/env python3
"""Document the im-not-ai reference relationship without copying upstream content.

This project intentionally reinterprets public high-level ideas for Korean report style.
Run this script to print the integration policy for maintainers.
"""
from __future__ import annotations

POLICY = """dorami-report-fmt uses a no-copy integration policy.

Allowed:
- Read im-not-ai to understand broad Korean prose cleanup categories.
- Rephrase ideas for objective Korean report style.
- Keep attribution and license notes in NOTICE.

Not allowed without explicit review:
- Copy upstream pattern tables, prompts, agent definitions, or code verbatim.
- Add copied content without preserving MIT attribution in NOTICE.
- Shift this project away from Korean report style refinement.
"""


def main() -> int:
    print(POLICY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
