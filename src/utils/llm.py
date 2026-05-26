
from src.core.config import mistral_api_key,mistral_model,mistral_temperature
from langchain_mistralai import ChatMistralAI

def get_llm():
    return ChatMistralAI(model = mistral_model, 
                         mistral_api_key = mistral_api_key,
                         temperature=mistral_temperature)