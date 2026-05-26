# 🎬 AI Video Assistant

AI Video Assistant is an end-to-end meeting intelligence system that converts long-form videos and meeting recordings into structured, searchable insights using LLMs, transcription pipelines, and hybrid Retrieval-Augmented Generation (RAG).

Built with:

- Streamlit
- LangChain
- Mistral AI
- Whisper
- ChromaDB
- Hybrid Retrieval (Vector + BM25)

---

# Features

## 🎙️ AI Transcription

Supports:

- Whisper (English transcription)
- Sarvam AI (Hinglish → English translation)

The system automatically processes:

- YouTube videos
- Local video/audio files

---

## 🧠 AI Summarization

Generates concise meeting summaries using:

- Map-reduce summarization
- LangChain pipelines
- Mistral AI

---

## 📌 Meeting Intelligence Extraction

Automatically extracts:

- ✅ Action Items
- 🔑 Key Decisions
- ❓ Open Questions

from raw meeting transcripts.

---

## 🔎 Hybrid RAG Pipeline

Uses:

- Chroma Vector Search
- BM25 Lexical Retrieval
- Ensemble Retrieval

to provide significantly better retrieval quality than standard vector-only RAG systems.

---

## 💬 Conversational Meeting Chat

Ask questions like:

- "What were the main decisions?"
- "Who owns the deployment task?"
- "What was discussed about RAG?"
- "What deadlines were mentioned?"

The assistant answers strictly from the meeting transcript context.

---

## 🎨 Custom Streamlit UI

Features:

- Modern cyberpunk-inspired UI
- Custom CSS design system
- Responsive layout
- Interactive chat interface
- Real-time pipeline status tracking

## 🚀 Installation

### 1. Clone the repository

[](https://github.com/AIAkashMukherjee/Advanced-RAG-Assistant#1-clone-the-repository)

```
git clone https://github.com/AIAkashMukherjee/Advanced-RAG-Assistant.git
```

```
cd Advanced-RAG-Assistant
```

### 2. Create virtual environment

```
python -m venv venv
```

```
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

# Tech Stack

## LLM / AI

- Mistral AI
- OpenAI Whisper
- Sarvam AI
- LangChain

## Retrieval / RAG

- ChromaDB
- HuggingFace Embeddings
- BM25 Retriever
- Ensemble Retriever

## Frontend

- Streamlit
- Custom CSS

## Audio / Video

- FFmpeg
- Pydub
- yt-dlp

---

# Supported Inputs

## YouTube URL

<pre class="overflow-visible! px-0!" data-start="3283" data-end="3326"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>https://youtube.com/watch?v=...</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

## Local File

<pre class="overflow-visible! px-0!" data-start="3343" data-end="3373"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>/path/to/video.mp4</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

Supported formats:

* mp4
* mp3
* wav
* mov
* mkv

# Environment Variables

Create a `.env` file:

<pre class="overflow-visible! px-0!" data-start="3067" data-end="3171"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>MISTRAL_API_KEY=your_mistral_api_key</span><br/><br/><span>SARVAM_API_KEY=your_sarvam_api_key</span><br/><br/><span>WHISPER_MODEL=small</span></code></pre></div></div></div></div></div></div></div></div></div></div></div></div></pre>

# RAG Pipeline

The application uses Hybrid Retrieval:

<pre class="overflow-visible! px-0!" data-start="3486" data-end="3624"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>Transcript</span><br/><span>    ↓</span><br/><span>Chunking</span><br/><span>    ↓</span><br/><span>Embeddings</span><br/><span>    ↓</span><br/><span>Chroma Vector Store</span><br/><span>    ↓</span><br/><span>BM25 + Vector Ensemble Retrieval</span><br/><span>    ↓</span><br/><span>LLM QA Chain</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

This improves:

* keyword retrieval
* semantic retrieval
* factual grounding
* answer precision

# Why This Project Matters

Most meeting assistants only:

* summarize transcripts
* provide basic QA

This project implements:

* production-style RAG architecture
* hybrid retrieval
* modular AI pipelines
* structured extraction workflows
* custom AI-native UI

making it significantly closer to real-world AI systems.

---

# License

MIT License

# Acknowledgements

* LangChain
* Streamlit
* Mistral AI
* OpenAI Whisper
* ChromaDB
* HuggingFace
