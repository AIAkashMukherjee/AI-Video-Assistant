from langchain_classic.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever
from langchain_core.documents import Document
from typing import List
from langchain_chroma import Chroma


def get_retriever(vector_store : Chroma, k :int = 4):
    return vector_store.as_retriever(
        search_type = 'similarity',
        search_kwargs = {"k":k}
    )


def build_hybrid_retriever(
    vector_store,
    documents: List[Document],
    k: int = 4,
    weights: list[float] = [0.6, 0.4],
):

    vector_retriever = (
        vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": k},
        )
    )

    bm25_retriever = (
        BM25Retriever.from_documents(
            documents
        )
    )

    return EnsembleRetriever(
        retrievers=[
            vector_retriever,
            bm25_retriever,
        ],
        weights=weights,
    )