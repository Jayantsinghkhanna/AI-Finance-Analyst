from tools.news_tool import (
    get_news
)


def news_fetch_skill(ticker):

    news = get_news(
        ticker
    )

    return news