from __future__ import annotations

import re

from .models import GroundedAnswer, RetrievedEvidence


CITATION_PATTERN = re.compile(r"\[([A-Za-z0-9_-]+)\]")


def extract_citations(text: str) -> list[str]:
    return CITATION_PATTERN.findall(text)


def validate_citations(answer: GroundedAnswer, evidence: list[RetrievedEvidence]) -> dict[str, object]:
    retrieved_ids = {item.source_id for item in evidence}
    inline = extract_citations(answer.answer)
    invalid = sorted({citation for citation in inline if citation not in retrieved_ids})
    declared_invalid = sorted({citation for citation in answer.citations if citation not in retrieved_ids})
    missing_inline = sorted({citation for citation in answer.citations if citation not in inline})
    return {
        "valid": not invalid and not declared_invalid and not missing_inline,
        "inline_citations": inline,
        "invalid_citations": invalid,
        "declared_invalid": declared_invalid,
        "missing_inline": missing_inline,
    }
