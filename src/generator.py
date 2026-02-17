from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from src.config import config

# Load tokenizer and model once (global, cached)
_tokenizer = AutoTokenizer.from_pretrained(config.LLM_MODEL_NAME)
_model = AutoModelForSeq2SeqLM.from_pretrained(config.LLM_MODEL_NAME)

# Move to CPU (or GPU if available)
_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
_model.to(_device)


def generate_answer(prompt: str) -> str:
    """
    Generate an answer using FLAN-T5.
    """
    inputs = _tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=config.MAX_PROMPT_TOKENS,
    ).to(_device)

    outputs = _model.generate(
        **inputs,
        max_new_tokens=config.MAX_NEW_TOKENS,
        do_sample=False,
    )

    answer = _tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer.strip()
