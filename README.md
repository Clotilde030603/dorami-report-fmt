# dorami-report-fmt

한국어 초안과 AI식 문장을 자연스럽고 객관적인 **도라미 보고서체**로 다듬는 AI writing skill입니다.

`dorami-report-fmt`의 FMT는 **Fit My Tone**을 뜻합니다. 사용자가 제공한 내용의 사실관계와 의미는 유지하면서 문장 표현, 문단 흐름, 제목 구조, 보고서식 어조를 정리합니다.

## 이런 때 사용하세요

- 보고서 초안이 어색하거나 AI가 쓴 것처럼 반복적으로 느껴질 때
- 메모를 객관적인 보고서 문체로 정리하고 싶을 때
- 구어체 문장을 단정한 보고서체로 바꾸고 싶을 때
- 제목, 소제목, 문단 흐름을 보고서 형식에 맞게 정리하고 싶을 때
- 원문 의미는 유지하면서 문장 표현만 자연스럽게 다듬고 싶을 때

## 이 스킬이 하는 일

- AI식 상투 표현을 줄입니다.
- 번역투와 어색한 문장을 정리합니다.
- 구어체를 보고서체로 바꿉니다.
- 제목, 소제목, 문단 흐름을 정돈합니다.
- 서론-본론-결론 구조로 정리할 수 있습니다.
- 객관적이고 신중한 보고서식 표현으로 다듬습니다.
- 초안의 의미를 유지하면서 문체와 흐름을 개선합니다.

## 이 스킬이 하지 않는 일

- 원문에 없는 사실을 추가하지 않습니다.
- 출처, 통계, 사례, 기관명, 법령을 임의로 만들지 않습니다.
- 사용자의 핵심 주장이나 의도를 마음대로 바꾸지 않습니다.
- 참고 문장이나 예시 문장을 그대로 복사하지 않습니다.

## 설치 방법

### Codex

```bash
mkdir -p ~/.agents/skills
cp -R skills/dorami-report-fmt ~/.agents/skills/dorami-report-fmt
```

프로젝트 단위로 사용하려면 이 저장소의 `.agents/skills/dorami-report-fmt/` 구조를 유지하면 됩니다.

### Claude Code

```bash
mkdir -p ~/.claude/skills
cp -R skills/dorami-report-fmt ~/.claude/skills/dorami-report-fmt
```

프로젝트 단위로 사용하려면 이 저장소의 `.claude/skills/dorami-report-fmt/` 구조를 유지하면 됩니다.

### 설치 스크립트 사용

```bash
./install.sh --codex
./install.sh --claude
./install.sh --all
```

## Gajae Code 및 기타 AI에서 사용

Gajae Code의 스킬 경로는 환경마다 다를 수 있습니다. 가능한 방식 중 하나를 사용하세요.

- 스킬 폴더 등록: `skills/dorami-report-fmt/`
- 커스텀 프롬프트 등록: `prompts/dorami-report-fmt-system-prompt.md`
- 수동 복붙: `portable/dorami-report-fmt.md`

ChatGPT, Claude, Gemini 등 일반 AI 도구에서는 `prompts/` 또는 `portable/` 폴더의 파일을 붙여넣어 사용할 수 있습니다.

## 사용 예시

```text
이 초안을 도라미 보고서체로 다듬어줘.
AI식 상투 표현은 줄이고, 객관적인 보고서 문체로 정리해줘.
내용은 임의로 추가하지 말고 문장 흐름과 표현만 다듬어줘.

[초안 붙여넣기]
```

```text
아래 메모를 보고서 형식으로 정리해줘.
서론-본론-결론 구조로 작성하고, 자연스러운 보고서체를 사용해줘.

[메모 붙여넣기]
```

```text
아래 문장을 구어체가 아니라 보고서 문체로 바꿔줘.
의미는 유지하고 표현만 정리해줘.

[문장 붙여넣기]
```

## 도라미 보고서체 기준

- 넓고 상투적인 도입부보다 보고서의 배경, 대상, 목적을 바로 제시합니다.
- 정책·보안·기술 주제는 `정의 → 현황 → 문제점/위험 → 개선방안/관리기준` 흐름으로 정리합니다.
- 시나리오형 내용은 `환경 → 흐름 → 영향 → 대응 방안` 순서로 구성합니다.
- 체크리스트형 내용은 점검 대상, 위험 요소, 확인 기준, 대응 조치를 구분합니다.
- 결론은 핵심 요약, 기대효과, 활용 가능성, 향후 검토 과제를 균형 있게 담습니다.
- “매우”, “획기적”, “필수불가결”처럼 근거 없는 과장 표현을 줄입니다.
- 같은 연결 표현과 종결어미가 반복되지 않도록 문장 구조를 조정합니다.

더 자세한 기준은 `skills/dorami-report-fmt/references/` 폴더에서 확인할 수 있습니다.

## 저장소 구조

```text
skills/dorami-report-fmt/   # 원본 스킬
.agents/skills/             # Codex 프로젝트 스킬
.claude/skills/             # Claude Code 프로젝트 스킬
prompts/                    # 복붙용 프롬프트
portable/                   # 단일 파일 버전
```

## 라이선스

MIT License
