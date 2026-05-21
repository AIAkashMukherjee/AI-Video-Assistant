from dotenv import load_dotenv
import os
load_dotenv()


WHISPER_MODEL=os.getenv('WHISPER_MODEL','small')
SARVAM_PIECE_SECONDS = 25

SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")
SARVAM_STT_TRANSLATE_URL = "https://api.sarvam.ai/speech-to-text-translate"
SARVAM_MODEL = os.getenv("SARVAM_STT_MODEL", "saaras:v2.5")

mistral_api_key = os.getenv("MISTRAL_API_KEY")
mistral_model = "mistral-small-latest"
mistral_temperature=0.3