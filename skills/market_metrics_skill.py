from tools.yfinance_tool import (
    get_stock_info
)


def market_metrics_skill(ticker):

    info = get_stock_info(
        ticker
    )

    return {

        "market_cap":
        info.get(
            "marketCap"
        ),

        "pe_ratio":
        info.get(
            "trailingPE"
        ),

        "sector":
        info.get(
            "sector"
        ),

        "beta":
        info.get(
            "beta"
        )
    }