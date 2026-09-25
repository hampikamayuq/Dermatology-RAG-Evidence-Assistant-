from __future__ import annotations

from dataclasses import dataclass

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .models import EvidenceCard, RetrievedEvidence


@dataclass
class TfidfRetriever:
    corpus: list[EvidenceCard]

    def __post_init__(self) -> None:
        self.vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
        documents = [f"{c.title} {' '.join(c.tags)} {c.text}" for c in self.corpus]
        self.matrix = self.vectorizer.fit_transform(documents)

    def search(self, query: str, top_k: int = 3, min_score: float = 0.02) -> list[RetrievedEvidence]:
        query_vector = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vector, self.matrix).ravel()
        ranked = scores.argsort()[::-1]

        results: list[RetrievedEvidence] = []
        for idx in ranked[:top_k]:
            score = float(scores[idx])
            if score < min_score:
                continue
            card = self.corpus[int(idx)]
            results.append(
                RetrievedEvidence(
                    source_id=card.source_id,
                    title=card.title,
                    score=round(score, 4),
                    text=card.text,
                )
            )
        return results
