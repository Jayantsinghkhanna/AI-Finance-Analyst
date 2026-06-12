from tools.yfinance_tool import (
    get_history
)

from tools.technical_tool import (
    calculate_rsi
)


def technical_analysis_skill(
    ticker
):

    df = get_history(
        ticker,
        period="1y"
    )

    rsi = calculate_rsi(
        df
    )

    sma50 = (
        df["Close"]
        .rolling(50)
        .mean()
        .iloc[-1]
    )

    sma200 = (
        df["Close"]
        .rolling(200)
        .mean()
        .iloc[-1]
    )

    trend = "Bullish"

    if sma50 < sma200:

        trend = "Bearish"

    return {

        "rsi": round(
            float(rsi),
            2
        ),

        "sma50": round(
            float(sma50),
            2
        ),

        "sma200": round(
            float(sma200),
            2
        ),

        "trend": trend
    }