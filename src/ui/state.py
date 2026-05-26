import streamlit as st

def init_session_state():
    """Initialize all session state variables"""
    for key, default in {
        "result": None,
        "chat_history": [],
        "pipeline_done": False,
        "pipeline_steps": {},
    }.items():
        if key not in st.session_state:
            st.session_state[key] = default


STEPS = [
    ("audio", "Audio"),
    ("transcript", "Transcribe"),
    ("title", "Title"),
    ("summary", "Summarise"),
    ("extract", "Extract"),
    ("rag", "RAG Index"),
]


def mark_step(key: str, state: str):
    """Mark a pipeline step as pending/active/done"""
    st.session_state.pipeline_steps[key] = state


def get_step_class(key: str) -> str:
    return st.session_state.pipeline_steps.get(key, "pending")


def get_step_icon(s: str) -> str:
    return {"pending": "·", "active": "▸", "done": "✓"}.get(s, "·")