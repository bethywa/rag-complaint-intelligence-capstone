import faiss
import pickle
from src.config import config


def load_faiss_store():
    """
    Load FAISS index and metadata from disk.
    """
    if not config.FAISS_INDEX_PATH.exists():
        raise FileNotFoundError(
            f"FAISS index not found at {config.FAISS_INDEX_PATH}"
        )

    index = faiss.read_index(str(config.FAISS_INDEX_PATH))

    with open(config.FAISS_METADATA_PATH, "rb") as f:
        metadata = pickle.load(f)

    return index, metadata
