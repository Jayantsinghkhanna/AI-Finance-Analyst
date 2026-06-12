from typing import TypedDict


class FinanceState(
    TypedDict,
    total=False
):

    query: str

    intent: str

    ticker: str

    executed_skills: list

    stock_price: dict

    market_metrics: dict

    financial_health: dict

    technical_analysis: dict

    news: list

    news_sentiment: dict

    risk_analysis: dict

    investment_summary: dict

    recommendation: dict

    report_date: str

    final_report: str

    pdf_path: str