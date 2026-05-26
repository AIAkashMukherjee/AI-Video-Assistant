import whisper
import os
from .sarvam import transcribe_chunk_sarvam
from src.core.config import WHISPER_MODEL


_model = None

def load_model():
    global _model  

    if _model is None: 
        print(f"Loading Whisper model: {WHISPER_MODEL} ...")
        _model = whisper.load_model(WHISPER_MODEL) 
        print("Whisper model loaded.")
    return _model 

def transcribe_chunk_whisper(chunk_path:str,translate:bool=False):
    model =load_model()

    result = model.transcribe(chunk_path,task='transcribe',fp16=False)

    return result["text"].strip()


# def transcribe_chunk(chunk_path: str, language: str = "english") -> str:
#     """
#     Route one chunk to Whisper or Sarvam depending on language choice.
#     - english  → Whisper (local model)
#     - hinglish → Sarvam (translates to English while transcribing)
#     """
#     if language.lower() == "hinglish":
#         return transcribe_chunk_sarvam(chunk_path)
#     return transcribe_chunk_whisper(chunk_path)



# def transcribe_all(chunks: list, translate:bool=False) -> str:
#     full_transcript = []

#     for i ,chunk in enumerate(chunks):
#         print(f"Transcribing chunk {i + 1}/{len(chunks)}...")

#         text = transcribe_chunk(chunk,translate=translate)  

#         full_transcript.append(text)

#     print("Transcription complete.")
#     return " ".join(full_transcript).strip()