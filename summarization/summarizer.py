from utils.llm import get_llm
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from prompts.summarization import MAP_SUMMARY_PROMPT,FINAL_SUMMARY_PROMPT
from preprocessing.splitter import split_transcript


def summarize(transcript: str) -> str:
    llm =get_llm()

    map_chain = MAP_SUMMARY_PROMPT | llm | StrOutputParser()

    chunks = split_transcript(transcript)

    chunk_summaries = [map_chain.invoke({"text" : chunk}) for chunk in chunks]

    combined = "\n\n".join(chunk_summaries)

    combined_chain = (
        RunnablePassthrough()
        | RunnableLambda(lambda x: {"text": x})
        | FINAL_SUMMARY_PROMPT
        | llm
        | StrOutputParser()
    )

    return combined_chain.invoke(combined)
