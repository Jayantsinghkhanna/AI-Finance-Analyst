from typing import TypedDict


class FinanceState(
    TypedDict,
    total=False
):

    # ======================
    # USER INPUT
    # ======================

    query: str

    intent: str

    ticker: str

    # ======================
    # AUTONOMY
    # ======================

    executed_skills: list

    next_skill: str

    enough_information: bool

    reflection_reasoning: str

    # ======================
    # SKILL OUTPUTS
    # ======================

    stock_price: dict

    market_metrics: dict

    financial_health: dict

    technical_analysis: dict

    news: list

    news_sentiment: dict

    risk_analysis: dict

    investment_summary: dict

    # ======================
    # FINAL OUTPUT
    # ======================

    recommendation: dict

    report_date: str

    final_report: str

    pdf_path: str