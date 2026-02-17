from dataclasses import dataclass
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

@dataclass(frozen=True)
class Config:
    EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
    LLM_MODEL_NAME: str = "google/flan-t5-base"

    # FAISS paths
    FAISS_INDEX_PATH: Path = BASE_DIR / "vector_store" / "faiss" / "index.faiss"
    FAISS_METADATA_PATH: Path = BASE_DIR / "vector_store" / "faiss" / "metadata.pkl"

    # RAG settings
    TOP_K: int = 5
    MAX_CONTEXT_CHARS: int = 1500
    MAX_PROMPT_TOKENS: int = 512
    MAX_NEW_TOKENS: int = 256


config = Config()
