"""
evaluation.py
--------------
Reusable qualitative evaluation utilities for the RAG pipeline.
"""

from typing import List, Dict
import pandas as pd
from src.pipeline import run_pipeline


def run_qualitative_evaluation(
    questions: List[str],
    k: int = 5
) -> pd.DataFrame:
    """
    Run qualitative evaluation for a list of questions.

    Args:
        questions (List[str]): Evaluation questions
        k (int): Number of retrieved chunks

    Returns:
        pd.DataFrame: Evaluation results table
    """
    records = []

    for q in questions:
        answer, sources = run_pipeline(q, k=k)

        records.append({
            "Question": q,
            "Generated Answer": answer,
            "Retrieved Sources": sources[:2],  # show top 1–2
            "Quality Score (1-5)": "",
            "Comments / Analysis": ""
        })

    return pd.DataFrame(records)


def save_evaluation(
    df: pd.DataFrame,
    path: str = "evaluation_results.csv"
):
    """
    Save evaluation results to disk.
    """
    df.to_csv(path, index=False)
