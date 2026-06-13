#!/usr/bin/env python3
"""Extract generalized style observations from private/redacted Markdown.

The output is intentionally aggregate and rule-oriented. It must remain under
private/style-analysis.md and should not include copied report paragraphs.
"""
from __future__ import annotations

import argparse
import re
import statistics
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRIVATE = ROOT / "private"
DEFAULT_SOURCE = PRIVATE / "redacted"
DEFAULT_OUT = PRIVATE / "style-analysis.md"

CONNECTORS = ["따라서", "이에 따라", "또한", "그러나", "반면", "이를 통해", "이로 인해", "그 결과", "나아가", "특히"]
REPORT_TERMS = ["현황", "문제", "위험", "대응", "개선", "관리", "보안", "정책", "시나리오", "체크리스트", "기대효과", "결론", "필요"]
CAUTIOUS_ENDINGS = ["필요가 있다", "요구된다", "고려해야 한다", "판단된다", "볼 수 있다", "가능성이 있다", "기대된다"]


def sentence_split(text: str) -> list[str]:
    # Keep this for metrics only; never write original sentences to output.
    parts = re.split(r"(?<=[.!?다요음임됨함됨])\s+|\n+", text)
    return [p.strip() for p in parts if len(p.strip()) > 8]


def classify_headings(headings: list[str]) -> Counter[str]:
    c: Counter[str] = Counter()
    for h in headings:
        if any(k in h for k in ["배경", "개요", "목적", "필요"]):
            c["배경·목적"] += 1
        if any(k in h for k in ["현황", "정의", "개념"]):
            c["정의·현황"] += 1
        if any(k in h for k in ["문제", "한계", "위험", "취약"]):
            c["문제·위험"] += 1
        if any(k in h for k in ["대응", "개선", "방안", "대책", "관리"]):
            c["대응·개선"] += 1
        if any(k in h for k in ["시나리오", "침해", "공격"]):
            c["시나리오"] += 1
        if any(k in h for k in ["체크", "점검", "항목"]):
            c["체크리스트"] += 1
        if any(k in h for k in ["결론", "기대", "효과", "활용"]):
            c["결론·기대효과"] += 1
    return c


def analyze(source: Path) -> str:
    files = sorted(source.glob("*.md"))
    all_text = "\n\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in files)
    headings = [m.group(1).strip() for m in re.finditer(r"^#{1,6}\s+(.+)$", all_text, re.M)]
    sentences = sentence_split(all_text)
    sentence_lengths = [len(s) for s in sentences]
    paragraph_lengths = [len(p.strip()) for p in re.split(r"\n\s*\n", all_text) if len(p.strip()) > 20]
    connector_counts = Counter({k: all_text.count(k) for k in CONNECTORS})
    term_counts = Counter({k: all_text.count(k) for k in REPORT_TERMS})
    cautious_counts = Counter({k: all_text.count(k) for k in CAUTIOUS_ENDINGS})
    heading_types = classify_headings(headings)
    table_lines = sum(1 for line in all_text.splitlines() if line.strip().startswith("|"))
    numbered = len(re.findall(r"^\s*\d+[.)]\s+", all_text, re.M))
    bullets = len(re.findall(r"^\s*[-*]\s+", all_text, re.M))

    def stat(values: list[int]) -> str:
        if not values:
            return "자료 부족"
        return f"평균 {statistics.mean(values):.1f}자, 중앙값 {statistics.median(values):.1f}자"

    dominant_headings = ", ".join(f"{k}({v})" for k, v in heading_types.most_common()) or "자료 부족"
    dominant_terms = ", ".join(f"{k}({v})" for k, v in term_counts.most_common(8) if v) or "자료 부족"
    dominant_connectors = ", ".join(f"{k}({v})" for k, v in connector_counts.most_common() if v) or "자료 부족"
    dominant_cautious = ", ".join(f"{k}({v})" for k, v in cautious_counts.most_common() if v) or "자료 부족"

    return f"""# private style analysis — dorami-report-fmt

주의: 이 파일은 로컬 참고용입니다. GitHub에 커밋하지 마세요. 아래 내용은 실제 예시 문장을 복사하지 않고, private/redacted 자료에서 추출한 집계적·일반화된 문체 관찰입니다.

## 분석 범위

- Markdown 파일 수: {len(files)}
- heading 수: {len(headings)}
- 표 형태 라인 수: {table_lines}
- 번호 목록 수: {numbered}
- 글머리표 수: {bullets}
- 문장 길이 경향: {stat(sentence_lengths)}
- 문단 길이 경향: {stat(paragraph_lengths)}

## 구조적 특징

- 소제목 유형 분포: {dominant_headings}
- 주요 주제어 분포: {dominant_terms}
- 자료는 배경·정의·현황에서 출발해 문제·위험을 설명하고, 대응·개선 또는 체크리스트로 정리하는 경향이 있다.
- 보안·정책·기술 주제에서는 개념 설명과 현황 정리 후 관리 필요성 또는 대응 기준으로 이어지는 구성이 두드러진다.
- 시나리오형 문서는 환경 설정, 행위 흐름, 피해 가능성, 대응 방안을 단계적으로 구분하는 방식이 적합하다.
- 체크리스트형 문서는 위험 요소와 점검 항목을 대응시키고, 표 또는 목록을 활용해 실무 적용성을 높이는 방식이 적합하다.

## 문체적 특징

- 자주 관찰된 연결 표현: {dominant_connectors}
- 신중한 결론 표현: {dominant_cautious}
- 객관적 보고서체는 단정적 감상보다 정의, 현황, 문제, 대응 기준을 순서대로 제시할 때 자연스럽다.
- 결론은 단순 요약보다 기대효과, 활용 가능성, 향후 검토 과제를 함께 정리하는 방식이 적합하다.
- 문장 길이는 너무 짧게 끊기보다 조건·원인·결과를 한 문단 안에서 연결하되, 긴 설명은 소제목과 목록으로 분리하는 방식이 적합하다.

## public 스킬 파일에 반영할 일반화 규칙

- 도입부는 넓은 일반론보다 보고서 주제의 배경, 대상, 목적을 바로 제시한다.
- 정책·보안·기술 설명은 정의 → 현황 → 문제점/위험 → 개선방안/관리기준 순서로 전개한다.
- 시나리오 설명은 환경 → 흐름 → 영향 → 대응 방안 순서로 정리한다.
- 체크리스트는 점검 대상, 위험 요소, 확인 기준, 대응 조치를 분리해 작성한다.
- 결론은 핵심 요약, 기대효과, 활용 가능성, 추가 검토 과제를 균형 있게 담는다.
- 같은 연결 표현과 종결어미가 반복되지 않도록 문장 구조를 조정한다.
- 실제 예시 문장은 public 문서에 복사하지 않고, 위와 같은 규칙으로만 반영한다.
"""


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Extract generalized style observations from private/redacted Markdown.")
    parser.add_argument("source", nargs="?", default=str(DEFAULT_SOURCE), help="private/redacted directory")
    args = parser.parse_args(argv)
    source = Path(args.source).resolve()
    if not str(source).startswith(str(PRIVATE.resolve())):
        print("Refusing to read outside private/.")
        return 2
    if not source.exists():
        print(f"Missing source directory: {source}")
        return 1
    DEFAULT_OUT.parent.mkdir(parents=True, exist_ok=True)
    DEFAULT_OUT.write_text(analyze(source), encoding="utf-8")
    print(f"wrote: {DEFAULT_OUT}")
    print("Reminder: private/style-analysis.md is local-only. Do not commit it to GitHub.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
