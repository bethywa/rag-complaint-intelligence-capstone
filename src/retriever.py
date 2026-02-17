from typing import List, Dict
import numpy as np
from sentence_transformers import SentenceTransformer
from src.config import config


_model = SentenceTransformer(config.EMBEDDING_MODEL_NAME)


def retrieve_chunks(index, metadata: List[Dict], query: str, k: int):
    query_vec = _model.encode([query]).astype("float32")
    distances, indices = index.search(query_vec, k)

    results = []
    for idx in indices[0]:
        record = metadata[idx]
        results.append({
            "text": record["document"],
            "metadata": record
        })

    return results
