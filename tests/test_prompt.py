# tests/test_prompt.py
from src.prompt import build_prompt

def test_prompt_contains_context_and_question():
    context = "Customer reports unauthorized charge."
    question = "What is the issue?"

    prompt = build_prompt(context, question)

    assert context in prompt
    assert question in prompt
    assert "Answer" in prompt
