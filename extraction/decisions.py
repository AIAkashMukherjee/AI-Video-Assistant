from extraction.base import build_extraction_chain
from prompts.extraction import KEY_DECISIONS_PROMPT


def extract_key_decisions(transcript: str) -> str:

    chain = build_extraction_chain(
        KEY_DECISIONS_PROMPT
    )

    return chain.invoke(transcript)