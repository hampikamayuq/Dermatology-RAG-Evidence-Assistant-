from __future__ import annotations

from pydantic import BaseModel, Field


class EvidenceCard(BaseModel):
    source_id: str
    title: str
    evidence_type: str
    year: int
    text: str
    tags: list[str] = Field(default_factory=list)


class RetrievedEvidence(BaseModel):
    source_id: str
    title: str
    score: float
    text: str


class GroundedAnswer(BaseModel):
    question: str
    answer: str
    citations: list[str]
    abstained: bool = False
