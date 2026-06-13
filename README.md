# dorami-report-fmt — 도라미 보고서체

`dorami-report-fmt`는 한국어 보고서 초안이나 메모를 자연스럽고 객관적인 보고서 문체로 다듬는 공개 배포용 AI 스킬 저장소입니다.

## 1. `dorami-report-fmt`란?

도라미 보고서체는 사용자가 제공한 한국어 문장, 메모, 초안을 보고서에 맞는 문체와 구조로 정리하는 스킬입니다. 과장된 표현, 구어체, 반복적인 문장 구조, AI식 상투 표현을 줄이고, 맥락·분석·시사점이 드러나도록 문단 흐름을 다듬습니다.

## 2. FMT = Fit My Tone 의미

FMT는 **Fit My Tone**의 약자입니다. 사용자가 제공한 의미와 사실관계를 유지하면서, 문체를 자연스럽고 객관적인 한국어 보고서체에 맞춥니다.

## 3. 이 스킬이 하는 일

- 한국어 보고서 초안을 객관적인 보고서 문체로 정리합니다.
- AI식 상투 표현과 부자연스러운 번역투를 완화합니다.
- 제목, 소제목, 문단 흐름, 연결 표현을 정돈합니다.
- 서론-본론-결론 또는 사용자가 지정한 목차에 맞게 구조화합니다.
- 근거가 부족한 내용은 단정하지 않고 신중한 표현으로 바꿉니다.

## 4. 이 스킬이 하지 않는 일

- 원문에 없는 사실, 통계, 기관명, 법령, 사례, 출처를 임의로 추가하지 않습니다.
- 실제 보고서 예시나 개인정보가 담긴 자료를 공개 저장소에 포함하지 않습니다.
- 참고 문장을 그대로 복사하지 않습니다.
- 목적을 문서 판별 시스템 회피로 설명하지 않습니다.

## 5. 왜 실제 예시 보고서가 포함되지 않는지

주의:
이 저장소는 공개 배포용이므로 실제 보고서 예시, HWP/HWPX 원본, 변환된 Markdown, 익명화된 예시 파일을 포함하지 않습니다.
개인 보고서 자료는 반드시 private/ 폴더에만 보관하고, GitHub에 업로드하지 마세요.

보고서에는 이름, 학교, 학번, 팀명, 이메일, 전화번호 등 식별 정보가 포함될 수 있습니다. 따라서 이 저장소는 공개 가능한 스킬 본체, 스타일 가이드, 템플릿, 설치 스크립트, 변환 도구, 개인정보 검사 도구만 포함합니다.

## 6. 설치 방법

```bash
./install.sh --codex
./install.sh --claude
./install.sh --all
```

제거:

```bash
./uninstall.sh --codex
./uninstall.sh --claude
./uninstall.sh --all
```

업데이트:

```bash
./update.sh
```

## 7. Codex에서 등록하는 방법

전역 스킬 등록:

```bash
mkdir -p ~/.agents/skills
cp -R skills/dorami-report-fmt ~/.agents/skills/dorami-report-fmt
```

프로젝트 스킬 등록:

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

## 8. Claude Code에서 등록하는 방법

전역 스킬 등록:

```bash
mkdir -p ~/.claude/skills
cp -R skills/dorami-report-fmt ~/.claude/skills/dorami-report-fmt
```

프로젝트 스킬 등록:

```text
.claude/skills/dorami-report-fmt/SKILL.md
```

사용 예시:

```text
도라미 보고서체 스킬을 사용해서 아래 초안을 보고서 문체로 다듬어줘.
```

## 9. Gajae Code에서 사용하는 방법

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

## 10. 기타 AI에서 사용하는 방법

ChatGPT, Claude, Gemini 등 일반 AI 도구에서는 다음 파일을 사용하세요.

- 시스템 또는 커스텀 지시문: `prompts/dorami-report-fmt-system-prompt.md`
- 매번 초안과 함께 붙여넣는 템플릿: `prompts/dorami-report-fmt-user-prompt.md`
- 짧은 요청: `prompts/dorami-report-fmt-short.md`
- 단일 파일 버전: `portable/dorami-report-fmt.md`


## 예시 자료를 사용해 스킬을 만드는 방식

이 저장소는 실제 보고서 예시 파일을 포함하지 않습니다. 다만 사용자는 로컬에서 자신의 HWP/HWPX 보고서를 Markdown으로 변환하고, 익명화한 뒤, 해당 자료를 분석하여 `style-guide.md`와 스킬 프롬프트를 개선할 수 있습니다.

흐름:

```text
HWP/HWPX 원본
→ private/source/
→ Markdown 변환
→ private/converted/
→ 개인정보 익명화
→ private/redacted/
→ 문체 분석
→ public style-guide/SKILL.md에 일반화된 규칙만 반영
→ 실제 예시 MD는 GitHub에 업로드하지 않음
```

명령어:

```bash
python tools/convert_hwp_to_markdown.py private/source
python tools/prepare_private_references.py private/converted
python tools/extract_style_from_private_refs.py private/redacted
```

실제 예시 MD 파일은 스킬 제작 과정에서만 사용하며, 공개 GitHub 저장소에는 포함하지 않습니다.
공개 저장소에는 예시 자료에서 추출한 문체 규칙만 포함합니다.

## 11. HWP/HWPX를 Markdown으로 변환하는 방법

이 기능은 로컬 전용입니다. 변환 결과는 반드시 `private/` 아래에 저장됩니다.

```bash
mkdir -p private/source
# private/source/ 안에 .hwp 또는 .hwpx 파일을 넣는다.

python tools/convert_hwp_to_markdown.py private/source
python tools/prepare_private_references.py private/converted
```

- 변환 결과는 `private/converted/`에 저장됩니다.
- 익명화 결과는 `private/redacted/`에 저장됩니다.
- 두 폴더 모두 로컬 전용이며 GitHub에 올라가지 않습니다.
- `.hwpx`는 가능한 경우 압축/XML 구조에서 텍스트를 추출합니다.
- `.hwp`는 `hwp5txt`, `hwp5html`, `pyhwp`, LibreOffice, pandoc 등 사용 가능한 도구를 확인합니다.
- 변환할 수 없으면 내용을 추측하지 않고 `private/conversion-notes.md`에 실패 원인을 기록합니다.

## 12. private/ 폴더 사용법

```text
private/source/     원본 HWP/HWPX, PDF, DOCX, TXT 등
private/converted/  변환된 Markdown
private/redacted/   익명화된 로컬 참고용 Markdown
```

로컬 예시는 문체와 구조 참고용이지 문장 복사용이 아닙니다. 공개 가능한 자료인지 사용자가 직접 확인해야 합니다.

## 13. 개인정보 및 공개 저장소 주의사항

절대 공개 저장소에 포함하지 마세요.

- `.hwp`, `.hwpx`
- 실제 보고서 원본
- HWP/HWPX에서 변환한 Markdown 파일
- 익명화한 예시 보고서 Markdown 파일
- 사용자의 실제 문체 예시 파일
- 개인정보가 포함된 파일
- `private/`, `local-references/`, `converted-examples/`, `redacted-examples/`, `raw/`, `tmp/`

## 14. 예시 프롬프트

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

## 15. 검증 스크립트 실행 방법

```bash
python skills/dorami-report-fmt/scripts/privacy_check.py .
python skills/dorami-report-fmt/scripts/validate_skill.py
python -m pytest tests
```

pytest가 없다면 설치하지 않아도 됩니다. 이 경우 앞의 두 검증 스크립트를 먼저 실행하고, pytest 미설치 사실을 기록하세요.

## 16. im-not-ai와의 관계

이 프로젝트는 `epoko77-ai/im-not-ai`의 한국어 AI식 표현 정리 아이디어를 참고할 수 있습니다. 다만 전체 내용을 복사하지 않고, 한국어 보고서 문체 정리와 보고서 형식 보정이라는 목적에 맞게 재구성합니다.

참고한 공개 정보:

- 저장소: <https://github.com/epoko77-ai/im-not-ai>
- 확인한 라이선스: MIT License

실제 코드나 문구를 가져오는 경우에는 반드시 `NOTICE`에 출처와 라이선스를 보존해야 합니다.

## 17. 라이선스 및 NOTICE

이 저장소는 MIT License로 배포됩니다. 자세한 내용은 `LICENSE`를 확인하세요.

이 저장소는 스킬 코드와 문서 템플릿을 제공합니다. 사용자가 자신의 보고서 자료를 넣어 사용할 경우 해당 자료의 권리와 개인정보 보호 책임은 사용자에게 있습니다. 공개 저장소에는 실제 사용자 보고서 예시가 포함되지 않습니다.
