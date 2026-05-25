from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

def split_transcript(
    transcript: str,
    chunk_size: int = 3000,
    chunk_overlap: int = 200,
) -> list[str]:

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    return splitter.split_text(transcript)

