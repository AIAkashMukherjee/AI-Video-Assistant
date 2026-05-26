from dotenv import load_dotenv
load_dotenv()
from src.utils.audio import process_input
from src.summarization.transcription.base import transcribe_all
from src.summarization.title_generator import generate_title
from src.summarization.summarizer import summarize

from src.extraction.action_items import extract_action_items
from src.extraction.decisions import extract_key_decisions
from src.extraction.questions import extract_questions

source = 'https://www.youtube.com/watch?v=T-D1OfcDW1M'
language ='english'

chunks=process_input(source)
transcript = transcribe_all(chunks=chunks,language=language)
print('*'*70)
print(transcript)


title = generate_title(transcript)
summary = summarize(transcript)

print("\n" + "=" * 60)
print(f"📌 TITLE: {title}")
print("=" * 60)
print("\n📋 SUMMARY")
print("-" * 60)
print(summary)



action_items = extract_action_items(transcript)
decisions = extract_key_decisions(transcript)
questions = extract_questions(transcript)

print("\n" + "=" * 60)
print("✅ ACTION ITEMS")
print("=" * 60)
print(action_items)

print("\n" + "=" * 60)
print("🔑 KEY DECISIONS")
print("=" * 60)
print(decisions)

print("\n" + "=" * 60)
print("❓ OPEN QUESTIONS")
print("=" * 60)
print(questions)