from extraction.base import build_extraction_chain
from prompts.extraction import ACTION_ITEMS_PROMPT


def extract_action_items(transcript: str) -> str:

    chain = build_extraction_chain(
        ACTION_ITEMS_PROMPT
    )

    return chain.invoke(transcript)