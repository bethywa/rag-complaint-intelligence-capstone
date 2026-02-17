from src.vector_store import load_faiss_store
from src.retriever import retrieve_chunks
from src.prompt import build_prompt
from src.generator import generate_answer
from src.utils import truncate_text
from src.config import config


def run_pipeline(question: str, k: int = config.TOP_K):
    index, metadata = load_faiss_store()

    retrieved = retrieve_chunks(index, metadata, question, k)
    context = "\n\n".join(r["text"] for r in retrieved)
    context = truncate_text(context, config.MAX_CONTEXT_CHARS)

    prompt = build_prompt(context, question)
    answer = generate_answer(prompt)

    return answer, retrieved


if __name__ == "__main__":
    q = "Why are customers complaining about credit card disputes?"
    answer, sources = run_pipeline(q)

    print("\nANSWER:\n", answer)
    print("\nSOURCES:\n", sources[:2])
