from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnableLambda,RunnablePassthrough
from utils.llm import get_llm

from prompts.title import TITLE_PROMPT


def generate_title(transcript: str) -> str:
    llm = get_llm()

    title_chain = (
        RunnablePassthrough()
        | RunnableLambda(lambda x: {"text": x})
        | TITLE_PROMPT
        | llm
        | StrOutputParser()
    )

    return title_chain.invoke(transcript[:2000])