from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda,RunnablePassthrough
from src.utils.llm import get_llm
from src.prompts.rag import RAG_PROMPT
from src.rag.vector_store import build_vector_store
from src.rag.retriever import build_hybrid_retriever
from src.rag.formatter import format_docs
from src.rag.ingestion import create_documents

def build_rag_chain(transcript: str):
    documents = create_documents(transcript)

    vector_store = build_vector_store(transcript)

    retriever = build_hybrid_retriever(vector_store=vector_store,documents=documents,k=6)

    llm = get_llm()

    rag_chain = (
        {
            "context": (
                retriever
                | RunnableLambda(format_docs)
            ),

            "question": RunnablePassthrough(),
        }
        | RAG_PROMPT
        | llm
        | StrOutputParser()
    )

    return rag_chain


# def load_rag_chain():

#     vector_store = load_vector_store()

#     retriever = get_retriever(
#         vector_store,
#         k=6,
#     )

#     llm = get_llm()

#     rag_chain = (
#         {
#             "context": (
#                 retriever
#                 | RunnableLambda(format_docs)
#             ),

#             "question": RunnablePassthrough(),
#         }
#         | RAG_PROMPT
#         | llm
#         | StrOutputParser()
#     )

#     return rag_chain