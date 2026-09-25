from derm_rag.answerer import MockGroundedAnswerer
from derm_rag.citations import validate_citations
from derm_rag.models import RetrievedEvidence


def test_generated_citations_are_valid():
    evidence = [
        RetrievedEvidence(source_id="SRC-1", title="Demo", score=0.7, text="Clinical assessment is appropriate when uncertainty is high."),
    ]
    answer = MockGroundedAnswerer().answer("question", evidence)
    result = validate_citations(answer, evidence)
    assert result["valid"] is True


def test_invalid_citation_is_detected():
    evidence = [
        RetrievedEvidence(source_id="SRC-1", title="Demo", score=0.7, text="Evidence text."),
    ]
    answer = MockGroundedAnswerer().answer("question", evidence)
    answer.answer += " Unsupported statement [SRC-99]."
    result = validate_citations(answer, evidence)
    assert result["valid"] is False
    assert "SRC-99" in result["invalid_citations"]
