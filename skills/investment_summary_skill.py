def investment_summary_skill(state):

    strengths = []
    weaknesses = []

    tech = state.get(
        "technical_analysis",
        {}
    )

    risk = state.get(
        "risk_analysis",
        {}
    )

    financial = state.get(
        "financial_health",
        {}
    )

    news = state.get(
        "news_sentiment",
        {}
    )

    if tech.get("trend") == "Bullish":

        strengths.append(
            "Bullish technical trend"
        )

    if financial.get(
        "profit_margin",
        0
    ) > 0.2:

        strengths.append(
            "Strong profitability"
        )

    if financial.get(
        "return_on_equity",
        0
    ) > 0.15:

        strengths.append(
            "Strong return on equity"
        )

    if risk.get(
        "risk_level"
    ) == "High":

        weaknesses.append(
            "High risk profile"
        )

    if financial.get(
        "debt_to_equity",
        0
    ) > 2:

        weaknesses.append(
            "High debt levels"
        )

    if (
        news.get(
            "sentiment",
            ""
        ).lower()
        in ["negative", "bearish"]
    ):

        weaknesses.append(
            "Negative news sentiment"
        )

    score = (
        len(strengths) * 20
        -
        len(weaknesses) * 10
        + 50
    )

    score = max(
        0,
        min(
            score,
            100
        )
    )

    return {

        "strengths":
        strengths,

        "weaknesses":
        weaknesses,

        "overall_score":
        score
    }