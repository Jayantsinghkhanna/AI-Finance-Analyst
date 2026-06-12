import numpy as np

from tools.yfinance_tool import (
    get_history,
    get_stock_info
)


def risk_analysis_skill(
    ticker
):

    df = get_history(
        ticker,
        period="1y"
    )

    returns = (
        df["Close"]
        .pct_change()
        .dropna()
    )

    volatility = (
        returns.std()
        * np.sqrt(252)
    )

    info = get_stock_info(
        ticker
    )

    beta = info.get(
        "beta",
        1
    )

    risk_level = "Low"

    if volatility > 0.4:

        risk_level = "High"

    elif volatility > 0.25:

        risk_level = "Medium"

    return {

        "volatility":
        round(
            float(volatility),
            3
        ),

        "beta": beta,

        "risk_level":
        risk_level
    }