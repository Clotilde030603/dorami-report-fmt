# dorami-report-fmt — 도라미 보고서체

`dorami-report-fmt`는 한국어 보고서 초안, 메모, AI식으로 어색한 문장을 **자연스럽고 객관적인 한국어 보고서체**로 다듬는 AI 스킬입니다.

FMT는 **Fit My Tone**의 약자입니다. 사용자가 제공한 사실관계와 의미를 유지하면서 문장 표현, 문단 흐름, 제목 구조를 도라미 보고서체에 맞게 정리합니다.

## 1. 이 스킬이 하는 일

- 한국어 보고서 초안을 객관적이고 단정한 보고서 문체로 다듬습니다.
- AI식 상투 표현, 반복적인 문장 구조, 부자연스러운 번역투를 줄입니다.
- 제목, 소제목, 문단 흐름, 연결 표현을 정리합니다.
- 메모나 초안을 보고서 형식으로 구조화합니다.
- 사용자가 제공한 내용의 사실관계는 유지합니다.
- 근거 없는 내용, 통계, 기관명, 사례, 출처를 임의로 추가하지 않습니다.

## 2. 이 스킬이 하지 않는 일

- 원문에 없는 사실을 만들어 넣지 않습니다.
- 보고서의 핵심 주장이나 의미를 임의로 바꾸지 않습니다.
- 개인정보가 담긴 실제 보고서 예시를 저장소에 포함하지 않습니다.
- 참고 문장이나 예시 문장을 그대로 복사하지 않습니다.
- 이 스킬의 목적을 문서 판별 시스템 회피로 설명하지 않습니다.

## 3. 빠른 사용 예시

```text
이 초안을 도라미 보고서체로 다듬어줘.
AI식 상투 표현은 줄이고, 보고서 문체로 자연스럽게 정리해줘.
내용은 임의로 추가하지 말고 문장 흐름과 표현만 정리해줘.

[초안 붙여넣기]
```

```text
아래 메모를 보고서 형식으로 정리해줘.
서론-본론-결론 구조로 작성하고, 객관적인 보고서체를 사용해줘.

[메모 붙여넣기]
```

```text
문체는 유지하되 AI가 쓴 것처럼 보이는 반복 표현과 상투적인 문장을 줄여줘.
근거 없는 내용은 추가하지 말고, 불확실한 부분은 신중한 표현으로 바꿔줘.

[초안 붙여넣기]
```

## 4. 설치 방법

### 전체 설치

```bash
./install.sh --all
```

### Codex만 설치

```bash
./install.sh --codex
```

### Claude Code만 설치

```bash
./install.sh --claude
```

### 제거

```bash
./uninstall.sh --all
```

### 업데이트

```bash
./update.sh
```

## 5. Codex에서 등록하는 방법

전역 스킬 등록:

```bash
mkdir -p ~/.agents/skills
cp -R skills/dorami-report-fmt ~/.agents/skills/dorami-report-fmt
```

프로젝트 스킬 등록 위치:

```text
.agents/skills/dorami-report-fmt/SKILL.md
```

사용 예시:

```text
이 초안을 dorami-report-fmt 스킬로 다듬어줘.
```

```text
도라미 보고서체로 보고서 문체를 정리해줘.
```

사용자의 Codex 환경에서 다른 스킬 경로를 사용한다면 `skills/dorami-report-fmt/`를 해당 custom skills 디렉터리에 복사하세요. 기본 원본은 항상 `skills/dorami-report-fmt/`입니다.

## 6. Claude Code에서 등록하는 방법

전역 스킬 등록:

```bash
mkdir -p ~/.claude/skills
cp -R skills/dorami-report-fmt ~/.claude/skills/dorami-report-fmt
```

프로젝트 스킬 등록 위치:

```text
.claude/skills/dorami-report-fmt/SKILL.md
```

사용 예시:

```text
도라미 보고서체 스킬을 사용해서 아래 초안을 보고서 문체로 다듬어줘.
```

## 7. Gajae Code에서 사용하는 방법

Gajae Code의 정확한 스킬 경로는 환경에 따라 다를 수 있으므로 단정하지 않습니다. 다음 방식 중 가능한 방식을 사용하세요.

### 1. 스킬 폴더 등록 방식

Gajae Code가 custom skill 폴더를 지원한다면 다음 폴더를 해당 스킬 디렉터리에 복사합니다.

```text
skills/dorami-report-fmt/
```

### 2. 프롬프트 등록 방식

Gajae Code가 custom prompt 또는 reusable instruction을 지원한다면 다음 파일을 등록합니다.

```text
prompts/dorami-report-fmt-system-prompt.md
```

### 3. 수동 복붙 방식

스킬 등록 기능이 없다면 다음 파일 내용을 붙여넣어 사용합니다.

```text
portable/dorami-report-fmt.md
```

## 8. 기타 AI에서 사용하는 방법

ChatGPT, Claude, Gemini 등 일반 AI 도구에서는 다음 파일을 사용할 수 있습니다.

- 시스템 또는 커스텀 지시문: `prompts/dorami-report-fmt-system-prompt.md`
- 초안과 함께 붙여넣는 템플릿: `prompts/dorami-report-fmt-user-prompt.md`
- 짧은 요청: `prompts/dorami-report-fmt-short.md`
- 단일 파일 버전: `portable/dorami-report-fmt.md`

## 9. 문체 기준

도라미 보고서체는 다음 기준을 따릅니다.

- 객관적이고 단정한 한국어 보고서체를 사용합니다.
- 넓고 상투적인 도입부보다 보고서의 배경, 대상, 목적을 바로 제시합니다.
- 정책·보안·기술 주제는 `정의 → 현황 → 문제점/위험 → 개선방안/관리기준` 흐름으로 정리합니다.
- 시나리오형 내용은 `환경 → 흐름 → 영향 → 대응 방안` 순서로 구성합니다.
- 체크리스트형 내용은 점검 대상, 위험 요소, 확인 기준, 대응 조치를 구분합니다.
- 결론은 핵심 요약, 기대효과, 활용 가능성, 향후 검토 과제를 균형 있게 담습니다.
- “매우”, “획기적”, “필수불가결”처럼 근거 없는 과장 표현을 줄입니다.
- 같은 연결 표현과 종결어미가 반복되지 않도록 문장 구조를 조정합니다.

자세한 기준은 `skills/dorami-report-fmt/references/` 폴더의 문서를 참고하세요.

## 10. 개인정보 및 공개 저장소 주의사항

주의:
이 저장소는 공개 배포용이므로 실제 보고서 예시, HWP/HWPX 원본, 변환된 Markdown, 익명화된 예시 파일을 포함하지 않습니다.
개인 보고서 자료는 GitHub에 업로드하지 마세요.

절대 공개 저장소에 포함하지 마세요.

- `.hwp`, `.hwpx`
- 실제 보고서 원본
- 보고서에서 변환한 Markdown 파일
- 익명화한 예시 보고서 Markdown 파일
- 사용자의 실제 문체 예시 파일
- 개인정보가 포함된 파일
- `private/`, `local-references/`, `converted-examples/`, `redacted-examples/`, `raw/`, `tmp/`

## 11. 검증 스크립트 실행 방법

공개 저장소에 올리기 전 다음 검증을 실행할 수 있습니다.

```bash
python skills/dorami-report-fmt/scripts/privacy_check.py .
python skills/dorami-report-fmt/scripts/validate_skill.py
python -m pytest tests
```

pytest가 없다면 설치하지 않아도 됩니다. 이 경우 앞의 두 검증 스크립트를 먼저 실행하고, pytest 미설치 사실을 기록하세요.

## 12. 개발자용 로컬 도구

일반 사용자는 이 섹션을 사용할 필요가 없습니다. 이 저장소에는 스킬 규칙을 유지보수하거나 공개 전 안전 검사를 할 때 쓰는 로컬 도구가 포함되어 있습니다.

- `skills/dorami-report-fmt/scripts/privacy_check.py`: 공개 저장소에 개인정보나 금지 파일이 들어갔는지 검사합니다.
- `skills/dorami-report-fmt/scripts/validate_skill.py`: 스킬 구조와 필수 파일을 검사합니다.
- `skills/dorami-report-fmt/scripts/sync_skill_entrypoints.py`: 원본 `SKILL.md`를 Codex/Claude Code 진입점과 동기화합니다.
- `tools/`: 유지보수자가 공개 전 점검과 규칙 관리를 위해 사용하는 보조 도구입니다. 도구 실행 결과나 개인 자료는 공개 저장소에 포함하지 않습니다.

## 13. im-not-ai와의 관계

이 프로젝트는 `epoko77-ai/im-not-ai`의 한국어 AI식 표현 정리 아이디어를 참고할 수 있습니다. 다만 전체 내용을 복사하지 않고, 한국어 보고서 문체 정리와 보고서 형식 보정이라는 목적에 맞게 재구성합니다.

참고한 공개 정보:

- 저장소: <https://github.com/epoko77-ai/im-not-ai>
- 확인한 라이선스: MIT License

실제 코드나 문구를 가져오는 경우에는 반드시 `NOTICE`에 출처와 라이선스를 보존해야 합니다.

## 14. 라이선스 및 NOTICE

이 저장소는 MIT License로 배포됩니다. 자세한 내용은 `LICENSE`를 확인하세요.

이 저장소는 스킬 코드와 문서 템플릿을 제공합니다. 사용자가 자신의 보고서 자료를 넣어 사용할 경우 해당 자료의 권리와 개인정보 보호 책임은 사용자에게 있습니다. 공개 저장소에는 실제 사용자 보고서 예시가 포함되지 않습니다.
