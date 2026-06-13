# 로컬 참고자료 사용 가이드

개인 보고서 예시는 공개 저장소에 올리지 않는다. 도라미 보고서체는 공개 가능한 규칙과 템플릿만 저장소에 포함하고, 개인 자료는 로컬 전용 폴더에서만 다룬다.

## 권장 폴더

- `private/source/`: 원본 HWP/HWPX, PDF, DOCX, TXT 등
- `private/converted/`: 변환된 Markdown
- `private/redacted/`: 익명화된 로컬 참고용 Markdown

`private/` 폴더는 `.gitignore`에 포함되어야 하며, GitHub에 업로드하지 않는다.

## 제거해야 할 정보

- 이름, 학교, 학번, 이메일, 전화번호, 생년월일
- 학과·전공 등 개인 식별 가능성이 있는 정보
- 팀명, 프로젝트명, 멘토명 등 작성자를 특정할 수 있는 정보
- 계좌번호, 주민등록번호, 주소 등 민감한 식별 정보

## 사용 원칙

- 로컬 예시는 문체와 구조 참고용이지 문장 복사용이 아니다.
- 공개 가능한 자료인지 사용자가 직접 확인해야 한다.
- 익명화 결과도 공개 저장소에 포함하지 않는다.
- 참고 문장의 표현을 그대로 복사하지 말고, 보고서 문체 규칙으로만 추상화한다.

## 로컬 예시를 분석해 스킬을 개선하는 흐름

개인 보고서 예시는 스킬 제작 및 로컬 사용 과정에서만 사용한다. HWP/HWPX를 Markdown으로 변환한 뒤, 익명화된 Markdown을 분석하여 스타일 가이드를 만들 수 있다.

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

사용자가 자신의 문체에 맞게 다시 만들고 싶다면 `private/source/`에 자신의 파일을 넣고 다음 명령을 실행한다.

```bash
python tools/convert_hwp_to_markdown.py private/source
python tools/prepare_private_references.py private/converted
python tools/extract_style_from_private_refs.py private/redacted
```

- 실제 Markdown 예시 파일은 GitHub에 올리지 않는다.
- 공개 배포물에는 예시 자료에서 추출한 문체 규칙만 포함한다.
- 예시 자료는 문체와 구조 참고용이지 문장 복사용이 아니다.
- `private/style-analysis.md`도 로컬 분석 결과이므로 커밋하지 않는다.
