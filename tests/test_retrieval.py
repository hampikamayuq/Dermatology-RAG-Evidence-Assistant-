from derm_rag.models import EvidenceCard
from derm_rag.retriever import TfidfRetriever


def test_retrieves_pigmented_lesion_card():
    corpus = [
        EvidenceCard(source_id="A", title="Pigmented lesion", evidence_type="demo", year=2026, text="changing pigmented lesion dermoscopy biopsy", tags=["melanoma"]),
        EvidenceCard(source_id="B", title="Dermatitis", evidence_type="demo", year=2026, text="itchy flexural dermatitis", tags=["eczema"]),
    ]
    results = TfidfRetriever(corpus).search("changing pigmented lesion dermoscopy", top_k=1)
    assert results[0].source_id == "A"


def test_abstains_when_no_retrieval_score():
    corpus = [
        EvidenceCard(source_id="A", title="Dermatitis", evidence_type="demo", year=2026, text="itchy flexural dermatitis", tags=[]),
    ]
    results = TfidfRetriever(corpus).search("quantum astronomy", top_k=1, min_score=0.5)
    assert results == []
