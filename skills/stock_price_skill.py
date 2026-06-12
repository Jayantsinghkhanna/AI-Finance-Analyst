from tools.yfinance_tool import (
    get_stock_info
)


def stock_price_skill(ticker):

    info = get_stock_info(
        ticker
    )

    return {

        "ticker": ticker,

        "price":
        info.get(
            "currentPrice"
        ),

        "previous_close":
        info.get(
            "previousClose"
        )
    }