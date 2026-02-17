# tests/test_generator.py
from src.generator import generate_answer

def test_generator_outputs_text():
    prompt = "Context: Customer dispute.\nQuestion: Why?\nAnswer:"
    answer = generate_answer(prompt)

    assert isinstance(answer, str)
    assert len(answer) > 0
