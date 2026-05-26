from langchain_community.embeddings import HuggingFaceEmbeddings
from src.core.config import EMBEDDING_MODEL


def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
    )