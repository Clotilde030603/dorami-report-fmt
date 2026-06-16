---
name: dorami-report-fmt
description: Rewrite Korean report drafts into a natural, objective, structured Korean report style. Use when the user asks to revise AI-like Korean report prose, fit a draft to a report style, reduce boilerplate phrasing, or format content as a polished Korean report.
---

# 도라미 보고서체

`dorami-report-fmt`는 사용자의 한국어 보고서 초안, 메모, 문장, AI식 문장을 객관적이고 자연스러운 보고서 문체로 다듬는 스킬이다. FMT는 **Fit My Tone**을 뜻하며, 사용자가 제공한 사실관계와 의미를 유지한 채 보고서에 맞는 문체와 구조로 정리한다.

## 사용 시점

다음과 같은 요청이 있을 때 이 스킬을 사용한다.

- “도라미 보고서체로 다듬어줘”
- “내 보고서체로 바꿔줘”
- “AI식 표현 줄여줘”
- “보고서 문체로 정리해줘”
- “보고서 구조로 바꿔줘”
- “문체는 유지하고 내용은 바꾸지 말아줘”
- “초안을 자연스럽게 다듬어줘”

## 작성 원칙

- 기본 출력은 한국어로 한다.
- 사용자가 제공한 사실관계와 의미는 유지한다.
- 근거 없는 내용, 통계, 기관명, 법령, 사례, 출처를 임의로 추가하지 않는다.
- 부족한 정보가 있으면 추측하지 말고 사용자에게 확인하거나 신중한 표현으로 처리한다.
- 보고서 문체에 맞게 제목, 문단, 연결 표현, 논리 흐름을 정리한다.
- 구어체, 과장 표현, 감정적인 표현, 홍보성 표현을 줄인다.
- “현대 사회에서 매우 중요한 문제로 대두되고 있다” 같은 상투적인 도입부를 피한다.
- 반복적인 문장 구조와 종결어미를 줄인다.
- 필요할 경우 “~로 볼 수 있다”, “~로 판단된다”, “~할 필요가 있다”, “~한 점에서 의미가 있다” 같은 신중한 보고서 표현을 사용한다.
- 예시 문서나 참고 문장을 그대로 복사하지 않는다.
- 이 스킬의 목적을 문서 판별 시스템 회피로 설명하지 않는다.
- `im-not-ai`를 별도 후처리로 실행하라고 안내하지 않는다.

## 작업 유형 구분

1. 사용자가 초안을 제공한 경우: 의미를 유지하면서 문체와 흐름을 다듬는다.
2. 사용자가 메모를 제공한 경우: 보고서 구조로 정리하되 없는 사실은 추가하지 않는다.
3. 문체만 수정하라고 한 경우: 내용과 구조 변경을 최소화한다.
4. 구조까지 수정하라고 한 경우: 제목, 소제목, 문단 순서를 정리한다.
5. AI식 표현을 줄이라고 한 경우: 상투 표현, 번역투, 반복 패턴을 완화한다.
6. 보고서 형식으로 작성하라고 한 경우: 서론-본론-결론 또는 사용자가 지정한 목차에 맞춘다.

## 작업 절차

1. 사용자의 목적을 확인한다: 문체 정리, 구조 정리, 메모의 보고서화, 문장 다듬기 중 무엇인지 파악한다.
2. 원문에서 보존해야 할 사실, 수치, 고유명사, 인용문을 먼저 식별한다.
3. `references/style-guide.md`와 `references/ai-like-phrasing-guide.md`를 기준으로 문장 리듬과 표현을 정리한다.
4. `references/do-not.md`에 있는 금지 항목을 피한다.
5. 구조 정리가 필요한 경우 `references/report-template.md`를 참고하되, 사용자의 원문에 없는 정보를 만들지 않는다.
6. 필요하면 마지막에 “수정 방향 요약”을 짧게 덧붙인다. 사용자가 본문만 원하면 요약은 생략한다.

## 출력 규칙

- 사용자의 원문이 짧으면 다듬은 문장만 간결하게 제공한다.
- 보고서 구조 요청이 있으면 제목과 소제목을 Markdown 헤딩으로 정리한다.
- 불확실한 내용은 “확인 필요”, “추가 근거가 필요하다”, “~로 해석될 수 있다”처럼 표시한다.
- 원문에 없는 사실을 추가해야만 문장이 성립하는 경우에는 본문에 넣지 말고 별도 확인 질문으로 남긴다.

## 도라미 보고서체 전개 규칙

- 도입부는 추상적인 일반론보다 보고서의 배경, 대상, 목적을 바로 제시한다.
- 정책·보안·기술 주제는 정의, 현황, 문제점/위험, 개선방안/관리기준 순서로 정리한다.
- 시나리오형 내용은 환경, 흐름, 영향, 대응 방안 순서로 구성한다.
- 체크리스트형 내용은 점검 대상, 위험 요소, 확인 기준, 대응 조치를 분리한다.
- 결론은 핵심 요약뿐 아니라 기대효과, 활용 가능성, 향후 검토 과제를 함께 정리한다.
- 같은 연결 표현과 종결어미가 반복되면 문장 구조와 문단 순서를 조정한다.
- 참고 문장이나 예시 문장을 그대로 복사하지 않고, 사용자가 제공한 원문의 의미를 유지한다.

## Internal editing flow

1. Preserve the original meaning and factual claims.
2. Identify the target report format and purpose.
3. Reduce generic AI-like phrasing, translationese, repetitive endings, and mechanical transitions as an internal writing guideline.
4. Apply Dorami report tone and report structure.
5. Review the result for objective Korean report style.
6. Do not recommend running `im-not-ai` as a separate post-processing step.
