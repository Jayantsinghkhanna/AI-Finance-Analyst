from skills.stock_price_skill import (
    stock_price_skill
)

from skills.market_metrics_skill import (
    market_metrics_skill
)

from skills.financial_health_skill import (
    financial_health_skill
)

from skills.technical_analysis_skill import (
    technical_analysis_skill
)

from skills.news_fetch_skill import (
    news_fetch_skill
)

from skills.news_sentiment_skill import (
    news_sentiment_skill
)

from skills.risk_analysis_skill import (
    risk_analysis_skill
)

from skills.investment_summary_skill import (
    investment_summary_skill
)


def finance_supervisor_agent(state):

    ticker = state["ticker"]

    intent = state["intent"]

    executed_skills = []

    print(
        "\n===== FINANCE SUPERVISOR ====="
    )

    # ----------------------------------
    # PRICE QUERY
    # ----------------------------------

    if intent == "price_lookup":

        state["stock_price"] = (
            stock_price_skill(
                ticker
            )
        )

        state["recommendation"] = {

            "recommendation":
            "INFO",

            "confidence":
            100,

            "reasoning":
            "Price lookup only."
        }

        return state

    # ----------------------------------
    # NEWS QUERY
    # ----------------------------------

    if intent == "news_lookup":

        state["news"] = (
            news_fetch_skill(
                ticker
            )
        )

        state["news_sentiment"] = (
            news_sentiment_skill(
                state["news"]
            )
        )

        state["recommendation"] = {

            "recommendation":
            "INFO",

            "confidence":
            100,

            "reasoning":
            "News lookup only."
        }

        return state

    # ----------------------------------
    # AUTONOMOUS LOOP
    # ----------------------------------

    required_skills = [

        "stock_price_skill",

        "market_metrics_skill",

        "financial_health_skill",

        "technical_analysis_skill",

        "news_fetch_skill",

        "news_sentiment_skill",

        "risk_analysis_skill"
    ]

    for skill in required_skills:

        if skill in executed_skills:
            continue

        print(
            f"\nRunning -> {skill}"
        )

        if skill == "stock_price_skill":

            state["stock_price"] = (
                stock_price_skill(
                    ticker
                )
            )

        elif skill == "market_metrics_skill":

            state["market_metrics"] = (
                market_metrics_skill(
                    ticker
                )
            )

        elif skill == "financial_health_skill":

            state["financial_health"] = (
                financial_health_skill(
                    ticker
                )
            )

        elif skill == "technical_analysis_skill":

            state["technical_analysis"] = (
                technical_analysis_skill(
                    ticker
                )
            )

        elif skill == "news_fetch_skill":

            state["news"] = (
                news_fetch_skill(
                    ticker
                )
            )

        elif skill == "news_sentiment_skill":

            state["news_sentiment"] = (
                news_sentiment_skill(
                    state["news"]
                )
            )

        elif skill == "risk_analysis_skill":

            state["risk_analysis"] = (
                risk_analysis_skill(
                    ticker
                )
            )

        executed_skills.append(
            skill
        )

    state["executed_skills"] = (
        executed_skills
    )

    # ----------------------------------
    # INVESTMENT SUMMARY
    # ----------------------------------

    state["investment_summary"] = (
        investment_summary_skill(
            state
        )
    )

    # ----------------------------------
    # SCORING ENGINE
    # ----------------------------------

    score = 50

    positives = []

    negatives = []

    financial = state.get(
        "financial_health",
        {}
    )

    technical = state.get(
        "technical_analysis",
        {}
    )

    sentiment = state.get(
        "news_sentiment",
        {}
    )

    risk = state.get(
        "risk_analysis",
        {}
    )

    # -------------------------
    # Profit Margin
    # -------------------------

    if financial.get(
        "profit_margin",
        0
    ) > 0.20:

        score += 15

        positives.append(
            "Strong profitability"
        )

    # -------------------------
    # ROE
    # -------------------------

    if financial.get(
        "return_on_equity",
        0
    ) > 0.15:

        score += 15

        positives.append(
            "Strong ROE"
        )

    # -------------------------
    # Technical Trend
    # -------------------------

    if technical.get(
        "trend"
    ) == "Bullish":

        score += 10

        positives.append(
            "Bullish trend"
        )

    # -------------------------
    # News Sentiment
    # -------------------------

    if sentiment.get(
        "sentiment",
        ""
    ).lower() in [

        "positive",

        "bullish"
    ]:

        score += 10

        positives.append(
            "Positive sentiment"
        )

    # -------------------------
    # Risk
    # -------------------------

    if risk.get(
        "risk_level"
    ) == "High":

        score -= 15

        negatives.append(
            "High risk"
        )

    # -------------------------
    # Debt
    # -------------------------

    if financial.get(
        "debt_to_equity",
        0
    ) > 2:

        score -= 10

        negatives.append(
            "High leverage"
        )

    score = max(
        0,
        min(
            score,
            100
        )
    )

    # ----------------------------------
    # FINAL RECOMMENDATION
    # ----------------------------------

    if score >= 70:

        recommendation = "BUY"

    elif score >= 50:

        recommendation = "HOLD"

    else:

        recommendation = "SELL"

    state["recommendation"] = {

        "recommendation":
        recommendation,

        "confidence":
        score,

        "reasoning":
        f"Recommendation generated using autonomous financial analysis. Final score = {score}.",

        "positives":
        positives,

        "negatives":
        negatives
    }

    print(
        "\nRECOMMENDATION:"
    )

    print(
        state["recommendation"]
    )

    return state