from datetime import datetime

from llm import llm


def report_agent(state):

    today = datetime.now().strftime(
        "%B %d, %Y"
    )

    state["report_date"] = today

    intent = state["intent"]

    # ==========================
    # PRICE LOOKUP
    # ==========================

    if intent == "price_lookup":

        stock = state.get(
            "stock_price",
            {}
        )

        report = f"""
{stock.get('ticker')} Stock Snapshot

Date: {today}

Ticker: {stock.get('ticker')}

Current Price:
${stock.get('price')}

Previous Close:
${stock.get('previous_close')}

This report was generated from live market data.
"""

        state["final_report"] = (
            report
        )

        return state

    # ==========================
    # NEWS LOOKUP
    # ==========================

    if intent == "news_lookup":

        news = state.get(
            "news",
            []
        )

        sentiment = state.get(
            "news_sentiment",
            {}
        )

        report = f"""
News Analysis Report

Date: {today}

Overall Sentiment:
{sentiment.get('sentiment', 'Unknown')}

News Headlines:

"""

        for item in news[:5]:

            report += (
                f"\n• {item}"
            )

        state["final_report"] = (
            report
        )

        return state

    # ==========================
    # FULL ANALYSIS
    # ==========================

    prompt = f"""
You are a professional equity research analyst.

Generate a detailed investment report.

Date:
{today}

User Query:
{state.get('query')}

Stock Price:
{state.get('stock_price')}

Market Metrics:
{state.get('market_metrics')}

Financial Health:
{state.get('financial_health')}

Technical Analysis:
{state.get('technical_analysis')}

News Sentiment:
{state.get('news_sentiment')}

Risk Analysis:
{state.get('risk_analysis')}

Recommendation:
{state.get('recommendation')}

Create these sections:

1. Executive Summary

2. Market Snapshot

3. Financial Health Analysis

4. Technical Analysis

5. News & Sentiment

6. Risk Assessment

7. Investment Recommendation

8. Confidence Score

9. Key Positives

10. Key Risks

Use professional analyst language.

Do not invent data.
"""

    response = (
        llm.invoke(
            prompt
        )
    )

    state["final_report"] = (
        response.content
    )

    return state