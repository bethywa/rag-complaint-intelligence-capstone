# tests/test_pipeline.py
from src.pipeline import run_pipeline

def test_pipeline_end_to_end():
    answer, sources = run_pipeline(
        "Why are customers complaining about credit card disputes?",
        k=3
    )

    assert isinstance(answer, str)
    assert len(answer) > 0
    assert isinstance(sources, list)
    assert len(sources) > 0
