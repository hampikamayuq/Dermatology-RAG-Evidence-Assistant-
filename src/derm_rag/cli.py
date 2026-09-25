from __future__ import annotations

import argparse
from pathlib import Path

from .answerer import MockGroundedAnswerer
from .citations import validate_citations
from .corpus import load_corpus
from .retriever import TfidfRetriever


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the dermatology RAG evidence demo")
    parser.add_argument("question")
    parser.add_argument("--corpus", default="data/synthetic_evidence_cards.json")
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--min-score", type=float, default=0.02)
    args = parser.parse_args()

    corpus_path = Path(args.corpus)
    corpus = load_corpus(corpus_path)
    retriever = TfidfRetriever(corpus)
    evidence = retriever.search(args.question, top_k=args.top_k, min_score=args.min_score)
    answer = MockGroundedAnswerer().answer(args.question, evidence)
    validation = validate_citations(answer, evidence)

    print("Retrieved evidence:")
    for item in evidence:
        print(f"- {item.source_id} | score={item.score:.4f} | {item.title}")
    print("\nAnswer:")
    print(answer.answer)
    print("\nCitation validation:")
    print(validation)


if __name__ == "__main__":
    main()
