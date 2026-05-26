def format_docs(docs) -> str:
    return "\n\n".join(
        [doc.page_content for doc in docs]
    )