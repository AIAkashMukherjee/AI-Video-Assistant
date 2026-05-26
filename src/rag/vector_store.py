from langchain_chroma import Chroma
from src.rag.embeddings import  get_embeddings
from src.rag.ingestion import create_documents
from src.core.config import COLLECTION_NAME,CHROMA_DIR


def build_vector_store( transcript: str) -> Chroma:
    print("Building vector store...")

    docs = create_documents(transcript)

    embeddings = get_embeddings()

    vector_store = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=CHROMA_DIR,
    )

    return vector_store

# def load_vector_store() -> Chroma:
#     embeddings = get_embeddings()

#     vector_store = Chroma(
#         collection_name=COLLECTION_NAME,
#         embedding_function=embeddings,
#         persist_directory=CHROMA_DIR,
#     )

#     return vector_store