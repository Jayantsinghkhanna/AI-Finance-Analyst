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


def skill_executor(
    state,
    skill
):

    ticker = state["ticker"]

    print(
        f"\nRunning Skill -> {skill}"
    )

    # ==========================
    # STOCK PRICE
    # ==========================

    if skill == "stock_price_skill":

        if "stock_price" not in state:

            state["stock_price"] = (
                stock_price_skill(
                    ticker
                )
            )

    # ==========================
    # MARKET METRICS
    # ==========================

    elif skill == "market_metrics_skill":

        if "market_metrics" not in state:

            state["market_metrics"] = (
                market_metrics_skill(
                    ticker
                )
            )

    # ==========================
    # FINANCIAL HEALTH
    # ==========================

    elif skill == "financial_health_skill":

        if "financial_health" not in state:

            state["financial_health"] = (
                financial_health_skill(
                    ticker
                )
            )

    # ==========================
    # TECHNICAL ANALYSIS
    # ==========================

    elif skill == "technical_analysis_skill":

        if "technical_analysis" not in state:

            state["technical_analysis"] = (
                technical_analysis_skill(
                    ticker
                )
            )

    # ==========================
    # NEWS FETCH
    # ==========================

    elif skill == "news_fetch_skill":

        if "news" not in state:

            state["news"] = (
                news_fetch_skill(
                    ticker
                )
            )

    # ==========================
    # NEWS SENTIMENT
    # ==========================

    elif skill == "news_sentiment_skill":

        if "news" not in state:

            state["news"] = (
                news_fetch_skill(
                    ticker
                )
            )

        if "news_sentiment" not in state:

            state["news_sentiment"] = (
                news_sentiment_skill(
                    state["news"]
                )
            )

    # ==========================
    # RISK ANALYSIS
    # ==========================

    elif skill == "risk_analysis_skill":

        if "risk_analysis" not in state:

            state["risk_analysis"] = (
                risk_analysis_skill(
                    ticker
                )
            )

    # ==========================
    # INVESTMENT SUMMARY
    # ==========================

    elif skill == "investment_summary_skill":

        state["investment_summary"] = (
            investment_summary_skill(
                state
            )
        )

    # ==========================
    # TRACK EXECUTED SKILLS
    # ==========================

    if "executed_skills" not in state:

        state["executed_skills"] = []

    if skill not in state["executed_skills"]:

        state["executed_skills"].append(
            skill
        )

    return state