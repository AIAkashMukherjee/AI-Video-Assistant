from extraction.base import build_extraction_chain
from prompts.extraction import QUESTIONS_PROMPT


def extract_questions(transcript: str) -> str:

    chain = build_extraction_chain(
        QUESTIONS_PROMPT
    )

    return chain.invoke(transcript)