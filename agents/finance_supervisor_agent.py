from agents.reflection_agent import (
    reflection_agent
)

from graph.skill_executor import (
    skill_executor
)


def finance_supervisor_agent(state):

    print(
        "\n===== FINANCE SUPERVISOR ====="
    )

    # ==========================
    # INITIALIZE
    # ==========================

    if "executed_skills" not in state:

        state["executed_skills"] = []

    max_iterations = 10

    iteration = 0

    # ==========================
    # AUTONOMOUS LOOP
    # ==========================

    while iteration < max_iterations:

        print(
            f"\n===== ITERATION {iteration + 1} ====="
        )

        # ----------------------
        # REFLECT
        # ----------------------

        state = (
            reflection_agent(
                state
            )
        )

        # ----------------------
        # STOP CONDITION
        # ----------------------

        if state[
            "enough_information"
        ]:

            print(
                "\nEnough information collected."
            )

            break

        # ----------------------
        # NEXT SKILL
        # ----------------------

        next_skill = (
            state.get(
                "next_skill"
            )
        )

        if not next_skill:

            print(
                "\nNo skill selected."
            )

            break

        # ----------------------
        # EXECUTE
        # ----------------------

        state = (
            skill_executor(
                state,
                next_skill
            )
        )

        iteration += 1

    # ==========================
    # SAFETY
    # ==========================

    if iteration >= max_iterations:

        print(
            "\nMaximum iterations reached."
        )

    # ==========================
    # RECOMMENDATION
    # ==========================

    state["recommendation"] = (
        generate_recommendation(
            state
        )
    )

    return state


def generate_recommendation(
    state
):

    confidence = 50

    positives = []

    negatives = []

    # ======================
    # FINANCIAL HEALTH
    # ======================

    financials = (
        state.get(
            "financial_health",
            {}
        )
    )

    profit_margin = (
        financials.get(
            "profit_margin",
            0
        )
    )

    if profit_margin > 20:

        confidence += 10

        positives.append(
            "Strong profit margins"
        )

    # ======================
    # TECHNICAL ANALYSIS
    # ======================

    technicals = (
        state.get(
            "technical_analysis",
            {}
        )
    )

    trend = (
        technicals.get(
            "trend",
            ""
        )
    )

    if trend == "Bullish":

        confidence += 10

        positives.append(
            "Bullish technical trend"
        )

    elif trend == "Bearish":

        confidence -= 10

        negatives.append(
            "Bearish technical trend"
        )

    # ======================
    # SENTIMENT
    # ======================

    sentiment = (
        state.get(
            "news_sentiment",
            {}
        )
    )

    sentiment_label = (
        sentiment.get(
            "sentiment",
            ""
        )
    )

    if sentiment_label == "Positive":

        confidence += 10

        positives.append(
            "Positive market sentiment"
        )

    elif sentiment_label == "Negative":

        confidence -= 10

        negatives.append(
            "Negative market sentiment"
        )

    # ======================
    # RISK
    # ======================

    risk = (
        state.get(
            "risk_analysis",
            {}
        )
    )

    beta = (
        risk.get(
            "beta",
            1
        )
    )

    if beta > 2:

        confidence -= 10

        negatives.append(
            "High volatility risk"
        )

    # ======================
    # FINAL DECISION
    # ======================

    if confidence >= 75:

        recommendation = "BUY"

    elif confidence >= 55:

        recommendation = "HOLD"

    else:

        recommendation = "SELL"

    return {
        "recommendation":
            recommendation,

        "confidence":
            confidence,

        "positives":
            positives,

        "negatives":
            negatives,

        "reasoning":
            (
                "Recommendation generated "
                "using autonomous skill "
                "execution and analysis."
            )
    }