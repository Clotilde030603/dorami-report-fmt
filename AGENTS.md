# AGENTS.md — dorami-report-fmt

이 저장소는 공개 배포용 한국어 보고서 문체 스킬 패키지다. 향후 AI 코딩 에이전트는 다음 규칙을 반드시 지킨다.

## 공개 저장소 안전 규칙

- raw HWP/HWPX 파일을 커밋하지 말 것.
- 변환된 보고서 예시 Markdown을 커밋하지 말 것.
- 사용자 고유 문체 예시를 커밋하지 말 것.
- `private/` 폴더는 항상 ignored 상태로 둘 것.
- `local-references/`, `converted-examples/`, `redacted-examples/`, `raw/`, `tmp/` 파일을 커밋하지 말 것.
- 개인정보 검사 스크립트를 약화하지 말 것.

## 스킬 구조 규칙

- 원본 스킬은 `skills/dorami-report-fmt/`에 둔다.
- `.agents/skills/dorami-report-fmt/SKILL.md`와 `.claude/skills/dorami-report-fmt/SKILL.md`는 원본과 동기화한다.
- 진입점 동기화에는 `skills/dorami-report-fmt/scripts/sync_skill_entrypoints.py`를 사용한다.

## 외부 참고 규칙

- `im-not-ai`에서 실제 내용을 가져온 경우 NOTICE에 출처와 라이선스 고지를 남길 것.
- 가능하면 문장이나 코드를 복사하지 말고, 한국어 보고서 문체 정리 규칙으로 재구성할 것.

## 목적 설명 규칙

- 이 스킬을 문서 판별 시스템 회피 목적으로 설명하지 말 것.
- “AI식 상투 표현 완화”, “부자연스러운 문장 정리”, “보고서 문체로 다듬기”로 설명할 것.
