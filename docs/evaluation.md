# Evaluating a medical RAG system

A useful evaluation separates retrieval quality from generation quality.

## Retrieval metrics

- Recall@k
- Precision@k
- Mean reciprocal rank (MRR)
- retrieval score distribution
- failure rate below the abstention threshold

## Generation metrics

- claim-level groundedness
- citation precision
- citation completeness
- unsupported-claim rate
- clinically important omission rate
- appropriate uncertainty / abstention

## Human review

For medical use, automated metrics should be complemented by blinded clinician review with explicit rubrics and inter-rater agreement. Evaluation datasets should represent the intended task and patient population rather than being treated as universally representative.
