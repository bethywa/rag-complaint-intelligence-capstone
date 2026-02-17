# tests/test_retriever.py
from src.vector_store import load_faiss_store
from src.retriever import retrieve_chunks

def test_retriever_returns_chunks():
    index, metadata = load_faiss_store()
    results = retrieve_chunks(index, metadata, "credit card dispute", k=3)

    assert isinstance(results, list)
    assert len(results) > 0
    assert "text" in results[0]
