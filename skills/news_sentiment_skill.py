from llm import llm

from schemas.sentiment_schema import (
    SentimentOutput
)


def news_sentiment_skill(
    news
):

    structured_llm = (
        llm.with_structured_output(
            SentimentOutput
        )
    )

    prompt = f"""
    Analyze the news.

    News:

    {news}
    """

    result = (
        structured_llm.invoke(
            prompt
        )
    )

    return (
        result.model_dump()
    )