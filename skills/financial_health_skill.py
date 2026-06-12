from tools.yfinance_tool import (
    get_stock_info
)


def financial_health_skill(
    ticker
):

    info = get_stock_info(
        ticker
    )

    return {

        "revenue":
        info.get(
            "totalRevenue"
        ),

        "net_income":
        info.get(
            "netIncomeToCommon"
        ),

        "profit_margin":
        info.get(
            "profitMargins"
        ),

        "debt_to_equity":
        info.get(
            "debtToEquity"
        ),

        "return_on_equity":
        info.get(
            "returnOnEquity"
        )
    }