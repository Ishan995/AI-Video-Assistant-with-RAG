from core.rag_engine import build_rag_context


def test_build_rag_context_uses_full_transcript_when_retrieval_is_empty():
    transcript = "The launch will happen on Friday. Alice will prepare the slides."
    context = build_rag_context(transcript, [])
    assert "The launch will happen on Friday" in context
    assert "Alice will prepare the slides" in context


def test_build_rag_context_includes_full_transcript_even_with_retrieval_docs():
    transcript = "The launch will happen on Friday. Alice will prepare the slides."
    docs = [type("Doc", (), {"page_content": "Friday launch"})()]
    context = build_rag_context(transcript, docs)
    assert "The launch will happen on Friday" in context
    assert "Friday launch" in context
