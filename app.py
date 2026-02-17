# =============================================================================
# app.py - Gradio Chatbot UI for Complaint Intelligence RAG
# =============================================================================

import sys
from pathlib import Path

# --------------------------------------------------
# Make `src` importable
# --------------------------------------------------
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

import gradio as gr
from src.pipeline import run_pipeline


# --------------------------------------------------
# Greeting detection
# --------------------------------------------------
def is_greeting(text: str) -> bool:
    greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]
    text = text.lower().strip()
    return any(text.startswith(g) for g in greetings)


# --------------------------------------------------
# Chat logic
# --------------------------------------------------
def chat(message: str, history: list, k: int = 5):
    """
    Main chat handler
    """
    if not message.strip():
        return "Please enter a question."

    # Friendly first response
    if is_greeting(message):
        return (
            "Hello! 👋\n\n"
            "I’m an **Analyst Assistant for CrediTrust**, a financial services company.\n"
            "I can help you analyze customer complaints related to credit cards, fraud, "
            "chargebacks, account closures, and more.\n\n"
            "How can I help you today?"
        )

    try:
        answer, sources = run_pipeline(message, k=k)
    except Exception as e:
        return f"Error running pipeline: {e}"

    # Format sources (show top 2)
    sources_text = ""
    for i, src in enumerate(sources[:2], start=1):
        company = src["metadata"].get("company", "Unknown company")
        text = src["text"][:300].replace("\n", " ")
        sources_text += f"\n\n**Source {i} ({company})**:\n{text}..."

    final_answer = f"{answer}\n\n---\n### Sources{sources_text}"
    return final_answer


# --------------------------------------------------
# Build Gradio UI (same UX as sample)
# --------------------------------------------------
def build_app():
    with gr.Blocks(
        title="CrediTrust Complaint Intelligence",
        css="""
        /* Make the whole page height fixed */
        body, html {
            height: 100%;
            margin: 0;
        }

        /* Chat container scrolls */
        #chat-container {
            height: calc(100vh - 140px);
            overflow-y: auto;
        }

        /* Fixed input area at bottom */
        #input-bar {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: white;
            padding: 10px;
            border-top: 1px solid #ddd;
            z-index: 100;
        }
        """
    ) as app:

        gr.Markdown("# 💳 CrediTrust Complaint Intelligence Assistant")

        # -------------------------------
        # Chat area (scrollable)
        # -------------------------------
        with gr.Column(elem_id="chat-container"):
            chatbot = gr.Chatbot(label="Chat", height=500)

        # -------------------------------
        # Fixed input bar
        # -------------------------------
        with gr.Row(elem_id="input-bar"):
            msg_input = gr.Textbox(
                placeholder="Ask a question about customer complaints...",
                show_label=False,
                scale=6,
            )
            send_btn = gr.Button("Ask", variant="primary", scale=1)
            clear_btn = gr.Button("Clear", scale=1)

        # -------------------------------
        # Event handlers
        # -------------------------------
        def respond(message, chat_history):
            answer = chat(message, chat_history, k=5)
            if chat_history is None:
                chat_history = []

            chat_history = chat_history + [
                gr.ChatMessage(role="user", content=message),
                gr.ChatMessage(role="assistant", content=answer),
            ]
            return "", chat_history

        def clear_chat():
            return []

        send_btn.click(
            fn=respond,
            inputs=[msg_input, chatbot],
            outputs=[msg_input, chatbot],
        )

        msg_input.submit(
            fn=respond,
            inputs=[msg_input, chatbot],
            outputs=[msg_input, chatbot],
        )

        clear_btn.click(
            fn=clear_chat,
            outputs=[chatbot],
        )

    return app



# --------------------------------------------------
# Main
# --------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("🚀 Starting CrediTrust Complaint Intelligence Chatbot")
    print("=" * 60)

    app = build_app()
    app.launch(theme=gr.themes.Soft())
