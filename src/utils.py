from typing import List

def truncate_text(text: str, max_chars: int) -> str:
    """
    Safely truncate text to avoid LLM context overflow.
    """
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "..."
