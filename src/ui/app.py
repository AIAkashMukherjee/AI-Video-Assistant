
import streamlit as st
import time
import sys
from pathlib import Path
ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.append(str(ROOT_DIR))
from src.utils.audio import process_input
from src.summarization.transcription.base import transcribe_all
from src.summarization.title_generator import generate_title
from src.summarization.summarizer import summarize
from src.extraction.action_items import extract_action_items
from src.extraction.decisions import extract_key_decisions
from src.extraction.questions import extract_questions
from src.rag.chain import build_rag_chain
from src.rag.qa import ask_question
from src.ui.styles import load_styles
from src.ui.state import init_session_state, mark_step
from src.ui.component import sidebar, page_header, display_results

load_styles()   # Load CSS

# Initialize session state
init_session_state()

# ── Sidebar ─────────────────────────────────────
source, language, run_btn = sidebar()

# ── Page Header ─────────────────────────────────
page_header()

# ── Pipeline Runner ─────────────────────────────
if run_btn:
    if not source.strip():
        st.error("Enter a YouTube URL or file path.")
    else:
        st.session_state.update({
            "pipeline_done": False, 
            "result": None,
            "chat_history": [], 
            "pipeline_steps": {}
        })
        
        notice = st.empty()
        notice.info("Pipeline running — check the sidebar for step status.")
        
        try:
            mark_step("audio", "active")
            chunks = process_input(source)
            mark_step("audio", "done")

            mark_step("transcript", "active")
            transcript = transcribe_all(chunks, language)
            mark_step("transcript", "done")

            mark_step("title", "active")
            title = generate_title(transcript)
            mark_step("title", "done")

            mark_step("summary", "active")
            summary = summarize(transcript)
            mark_step("summary", "done")

            mark_step("extract", "active")
            action_items = extract_action_items(transcript)
            decisions = extract_key_decisions(transcript)
            questions = extract_questions(transcript)
            mark_step("extract", "done")

            mark_step("rag", "active")
            rag_chain = build_rag_chain(transcript)
            mark_step("rag", "done")

            st.session_state.result = {
                "title": title,
                "transcript": transcript,
                "summary": summary,
                "action_items": action_items,
                "key_decisions": decisions,
                "open_questions": questions,
                "rag_chain": rag_chain,
            }
            st.session_state.pipeline_done = True
            notice.success("✓ Analysis complete.")
            time.sleep(0.6)
            notice.empty()
            st.rerun()

        except Exception as e:
            for k in st.session_state.pipeline_steps:
                if st.session_state.pipeline_steps[k] == "active":
                    st.session_state.pipeline_steps[k] = "pending"
            notice.error(f"Error: {e}")

# ── Display Results ─────────────────────────────
if st.session_state.result:
    r = st.session_state.result
    user_input, send = display_results(r)

    if send and user_input.strip():
        with st.spinner("Thinking…"):
            answer = ask_question(r["rag_chain"], user_input.strip())
        
        st.session_state.chat_history += [
            {"role": "user", "content": user_input.strip()},
            {"role": "assistant", "content": answer},
        ]
        st.rerun()

    if st.session_state.chat_history:
        if st.button("Clear chat", type="secondary"):
            st.session_state.chat_history = []
            st.rerun()

else:
    # Empty State
    st.markdown("""
    <div class="empty-state">
        <div class="empty-big">Drop a meeting in.</div>
        <div class="empty-sub">
            Paste a YouTube URL or local file path in the sidebar, pick a language, and hit Analyse.
        </div>
        <div>
            <span class="pill pill-y">Transcription</span>
            <span class="pill pill-g">Summarisation</span>
            <span class="pill pill-o">RAG Chat</span>
        </div>
    </div>""", unsafe_allow_html=True)