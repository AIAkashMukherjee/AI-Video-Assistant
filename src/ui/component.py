import streamlit as st
import html
from .state import STEPS, get_step_class, get_step_icon

def escape(text: str) -> str:
    return html.escape(str(text))


def sidebar():
    with st.sidebar:
        st.markdown('<div class="sidebar-brand">Rec·AP</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-sub">Meeting Intelligence</div>', unsafe_allow_html=True)
        
        source = st.text_input("URL or file path", placeholder="https://youtube.com/... or /path/to/file.mp4")
        language = st.selectbox("Language", ["english", "hinglish"], index=0)
        run_btn = st.button("⚡ Analyse", use_container_width=True)

        if st.session_state.pipeline_done or st.session_state.pipeline_steps:
            st.markdown("<hr style='border-color:#222!important;margin:1rem 0!important'>", unsafe_allow_html=True)
            for key, label in STEPS:
                s = get_step_class(key)
                st.markdown(f"""
                <div class="step-row {s}">
                    <div class="step-icon {s}">{get_step_icon(s)}</div>
                    <span>{label}</span>
                </div>""", unsafe_allow_html=True)
        
        return source, language, run_btn


def page_header():
    st.markdown('<div class="page-eyebrow">AI Video Assistant</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Transcribe.<br><em>Understand.</em><br>Ask anything.</div>', unsafe_allow_html=True)
    st.markdown("---")


def display_results(r):
    # Session Title
    st.markdown(f"""
    <div class="session-title-wrap">
        <div class="session-label">Session</div>
        <div class="session-title">{escape(r['title'])}</div>
    </div>""", unsafe_allow_html=True)

    # Summary + Transcript
    col_s, col_t = st.columns([3, 2], gap="large")
    with col_s:
        st.markdown(f"""
        <div class="summary-block">
            <div class="blabel" style="padding-left:2.5rem">Summary</div>
            <div style="padding-left:2.5rem">{escape(r['summary'])}</div>
        </div>""", unsafe_allow_html=True)

    with col_t:
        with st.expander("Full transcript", expanded=False):
            st.markdown(f'<div class="tbox">{escape(r["transcript"])}</div>', unsafe_allow_html=True)

    st.markdown("<div style='margin-top:1.5rem'></div>", unsafe_allow_html=True)

    # Extraction Cards
    c1, c2, c3 = st.columns(3, gap="medium")
    cards = [
        (c1, "Action Items", r['action_items'], "tag-yellow"),
        (c2, "Key Decisions", r['key_decisions'], "tag-green"),
        (c3, "Open Questions", r['open_questions'], "tag-orange"),
    ]

    for col, label, content, tag_cls in cards:
        with col:
            st.markdown(f"""
            <div class="extract-card">
                <div class="elabel">
                    <span class="etag {tag_cls}"></span>
                    {label}
                </div>
                <div class="econtent">{escape(content)}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("---")

    # Chat Interface
    st.markdown('<div style="font-family:\'DM Serif Display\',serif;font-size:1.35rem;margin-bottom:1rem">Chat with your meeting</div>', unsafe_allow_html=True)

    if st.session_state.chat_history:
        chat_html = '<div class="chat-wrap">'
        for msg in st.session_state.chat_history:
            safe = escape(msg["content"])
            if msg["role"] == "user":
                chat_html += f"""
                <div class="chat-row clearfix">
                    <div class="chat-who u">You</div>
                    <div class="chat-bubble bubble-u">{safe}</div>
                </div>"""
            else:
                chat_html += f"""
                <div class="chat-row clearfix">
                    <div class="chat-who b">Assistant</div>
                    <div class="chat-bubble bubble-b">{safe}</div>
                </div>"""
        chat_html += "</div>"
        st.markdown(chat_html, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background:var(--surface);border:1px solid var(--rule);border-radius:10px;
             padding:1.5rem;text-align:center;color:var(--ink-3);font-size:0.85rem;margin-bottom:0.75rem">
            Ask a question about the transcript above.
        </div>""", unsafe_allow_html=True)

    # Question Input
    q_col, btn_col = st.columns([5, 1], gap="small")
    with q_col:
        user_input = st.text_input("Question", placeholder="What decisions were made?", label_visibility="collapsed")
    with btn_col:
        send = st.button("Send →", use_container_width=True)

    return user_input, send