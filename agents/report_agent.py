from datetime import datetime

from llm import llm


def report_agent(state):

    today = datetime.now().strftime(
        "%B %d, %Y"
    )

    state["report_date"] = today

    recommendation = state.get(
        "recommendation",
        {}
    )

    stock_price = state.get(
        "stock_price",
        {}
    )

    market_metrics = state.get(
        "market_metrics",
        {}
    )

    financial_health = state.get(
        "financial_health",
        {}
    )

    technical_analysis = state.get(
        "technical_analysis",
        {}
    )

    news_sentiment = state.get(
        "news_sentiment",
        {}
    )

    risk_analysis = state.get(
        "risk_analysis",
        {}
    )

    prompt = f"""
Generate a professional equity research report.

Date:
{today}

Ticker:
{state.get('ticker')}

Recommendation:
{recommendation}

Stock Price:
{stock_price}

Market Metrics:
{market_metrics}

Financial Health:
{financial_health}

Technical Analysis:
{technical_analysis}

News Sentiment:
{news_sentiment}

Risk Analysis:
{risk_analysis}

Create a report with EXACTLY these sections:

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

Use professional investment analyst language.
Do not invent data.
Use only supplied information.
"""

    response = llm.invoke(
        prompt
    )

    state["final_report"] = (
        response.content
    )

    return state    