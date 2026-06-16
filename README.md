# dorami-report-fmt

한국어 초안과 AI식 문장을 자연스럽고 객관적인 도라미 보고서체로 다듬는 AI writing skill입니다.

## dorami-report-fmt란?

`dorami-report-fmt`는 한국어 보고서 초안, 메모, AI식 문장을 보고서 문체로 정리하는 스킬입니다.

문장 표현, 문단 흐름, 제목 구조, 보고서식 어조를 다듬고, 사용자가 제공한 내용의 사실관계와 의미는 유지합니다.

원문에 없는 사실, 통계, 사례, 출처는 임의로 추가하지 않습니다.

Codex, Claude Code, Gajae Code, 일반 AI 도구에서 사용할 수 있도록 구성되어 있습니다.

## 주요 기능

- AI식 상투 표현 완화
- 번역투와 어색한 문장 정리
- 구어체를 보고서체로 변환
- 제목, 소제목, 문단 흐름 정리
- 서론-본론-결론 구조화
- 객관적이고 신중한 보고서식 표현으로 수정
- 초안의 의미를 유지하면서 문체와 흐름 개선

## 하지 않는 일

- 원문에 없는 사실을 추가하지 않습니다.
- 출처, 통계, 사례를 임의로 만들지 않습니다.
- 실제 보고서 예시 파일을 공개 저장소에 포함하지 않습니다.
- 문서 판별 시스템 회피 목적으로 설명하지 않습니다.
- `im-not-ai`를 별도로 실행하라고 안내하지 않습니다.

## 설치

### Codex

```bash
mkdir -p ~/.agents/skills
cp -R skills/dorami-report-fmt ~/.agents/skills/dorami-report-fmt
```

프로젝트 단위로 사용하려면 `.agents/skills/dorami-report-fmt/` 구조를 유지합니다.

### Claude Code

```bash
mkdir -p ~/.claude/skills
cp -R skills/dorami-report-fmt ~/.claude/skills/dorami-report-fmt
```

프로젝트 단위로 사용하려면 `.claude/skills/dorami-report-fmt/` 구조를 유지합니다.

### 설치 스크립트

```bash
./install.sh --codex
./install.sh --claude
./install.sh --all
```

## Gajae Code 및 기타 AI에서 사용

Gajae Code의 정확한 스킬 경로는 환경마다 다를 수 있으므로 다음 방식 중 가능한 방식을 사용합니다.

- 스킬 폴더 등록: `skills/dorami-report-fmt/`
- 커스텀 프롬프트 등록: `prompts/dorami-report-fmt-system-prompt.md`
- 수동 복붙: `portable/dorami-report-fmt.md`

일반 AI 도구에서는 `prompts/` 또는 `portable/` 폴더의 파일을 사용합니다.

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

## 내부 처리 흐름

```text
원문 의미 보존
→ AI식 상투 표현과 번역투 완화
→ 도라미 보고서체 적용
→ 제목/문단 흐름 정리
→ 최종 보고서 문체 검수
```

## im-not-ai와의 관계

`dorami-report-fmt`는 `im-not-ai`를 별도로 실행하는 방식이 아닙니다.

도라미 보고서체로 문장을 다듬는 과정 안에 AI식 상투 표현, 번역투, 반복 문장 구조를 줄이는 규칙이 함께 포함되어 있습니다.

`im-not-ai`는 한국어 AI식 표현 완화 아이디어를 참고할 수 있는 관련 프로젝트이며, 이 저장소는 해당 방향성을 한국어 보고서 문체와 구조 정리에 맞게 재구성합니다.

## 저장소 구조

```text
skills/dorami-report-fmt/   # 원본 스킬
.agents/skills/             # Codex 프로젝트 스킬
.claude/skills/             # Claude Code 프로젝트 스킬
prompts/                    # 복붙용 프롬프트
portable/                   # 단일 파일 버전
tools/                      # 개발 및 검증 보조 도구
tests/                      # 검증 테스트
```

## 개발 문서

문체 추출 루프, HWP/HWPX 변환 도구, 벤치마크 설계는 스킬 제작과 검증을 위한 개발 문서로 분리되어 있습니다.

일반 사용자는 README의 설치 및 사용 예시만 참고하면 됩니다.

- `skills/dorami-report-fmt/references/style-extraction-loop.md`
- `skills/dorami-report-fmt/references/benchmark-guide.md`
- `skills/dorami-report-fmt/references/local-reference-guide.md`

## 검증

```bash
python3 skills/dorami-report-fmt/scripts/privacy_check.py .
python3 skills/dorami-report-fmt/scripts/validate_skill.py
python3 -m py_compile tools/*.py skills/dorami-report-fmt/scripts/*.py tests/*.py
```

## 라이선스

MIT License.
