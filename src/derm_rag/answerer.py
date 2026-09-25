from __future__ import annotations

import re

from .models import GroundedAnswer, RetrievedEvidence


class MockGroundedAnswerer:
    """Deterministic answerer used to demonstrate grounding and citation flow."""

    def answer(self, question: str, evidence: list[RetrievedEvidence]) -> GroundedAnswer:
        if not evidence:
            return GroundedAnswer(
                question=question,
                answer="Insufficient retrieved evidence to answer this question.",
                citations=[],
                abstained=True,
            )

        statements: list[str] = []
        citations: list[str] = []
        for item in evidence[:2]:
            sentence = re.split(r"(?<=[.!?])\s+", item.text.strip())[0].strip()
            if sentence and sentence[-1] not in ".!?":
                sentence += "."
            statements.append(f"{sentence} [{item.source_id}]")
            citations.append(item.source_id)

        return GroundedAnswer(
            question=question,
            answer=" ".join(statements),
            citations=citations,
            abstained=False,
        )
