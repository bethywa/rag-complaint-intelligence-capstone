import pickle
import pandas as pd
import numpy as np
import faiss
from pathlib import Path
from src.config import config


def build_faiss_index():
    print("📦 Loading embeddings parquet...")
    df = pd.read_parquet(config.DATA_PATH)

    embeddings = np.vstack(df["embedding"].values).astype("float32")
    metadata = df.drop(columns=["embedding"]).to_dict(orient="records")

    print("🧠 Building FAISS index...")
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    config.FAISS_DIR.mkdir(parents=True, exist_ok=True)

    faiss.write_index(index, str(config.FAISS_INDEX_PATH))
    with open(config.METADATA_PATH, "wb") as f:
        pickle.dump(metadata, f)

    print(f"✅ Indexed {index.ntotal} vectors")
    print("🎉 FAISS index saved successfully")


if __name__ == "__main__":
    build_faiss_index()
