from dotenv import load_dotenv
load_dotenv()
from utils.audio import process_input
from transcription.base import transcribe_all

source = 'https://www.youtube.com/watch?v=WDnzZlJjkOc'
language ='hinglish'

chunks=process_input(source)
transcript = transcribe_all(chunks=chunks,language=language)
print('*'*70)
print(transcript)
