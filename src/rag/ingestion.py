from langchain_core.documents import  Document

from preprocessing.splitter import  split_transcript


def create_documents(transcript: str) -> list[Document]:

    chunks = split_transcript(
        transcript,
        chunk_size=600,
        chunk_overlap=90,
    )

    docs = [
        Document(
            page_content=chunk,
            metadata={"chunk_index": i},
        )
        for i, chunk in enumerate(chunks)
    ]

    return docs