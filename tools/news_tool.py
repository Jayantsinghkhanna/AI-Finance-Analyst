from ddgs import DDGS


def get_news(query):

    with DDGS() as ddgs:

        results = list(
            ddgs.text(
                f"{query} stock news",
                max_results=5
            )
        )

    return results