# tests/test_vector_store.py
from src.vector_store import load_faiss_store

def test_faiss_store_loads():
    index, metadata = load_faiss_store()
    assert index is not None
    assert metadata is not None
    assert len(metadata) > 0
