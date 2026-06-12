# 🚀 Autonomous Finance Analyst

An Autonomous Finance Analyst built using LangGraph, Gemini, Agent Skills, and yFinance that performs live financial analysis, sentiment analysis, risk assessment, investment recommendations, and automated PDF report generation.

---

# 🎯 Overview

This project simulates a professional financial analyst by autonomously gathering market information, evaluating company fundamentals, analyzing sentiment and risk, and generating investment recommendations.

Unlike traditional LLM applications, the system dynamically decides what information it needs before generating an answer.

---

# 🧠 Architecture

```text
User Query
     │
     ▼

Router Agent
(Intent Detection)

     │
     ▼

Finance Supervisor Agent
(Autonomous Reasoning)

     │
     ▼

Reflection Agent

     │
     ▼

Choose Next Skill

     │
     ▼

Skill Executor

     │
     ▼

Agent Skills

     ├── Stock Price Skill
     ├── Market Metrics Skill
     ├── Financial Health Skill
     ├── Technical Analysis Skill
     ├── News Fetch Skill
     ├── News Sentiment Skill
     └── Risk Analysis Skill

     │
     ▼

Recommendation Engine

     │
     ▼

Report Agent

     │
     ▼

PDF Report Generator

     │
     ▼

Investment_Report.pdf
```

---

# 🤖 Agents

## Router Agent

Uses Gemini + Pydantic to:

* Detect intent
* Extract ticker symbols
* Route user requests

Example:

```json
{
  "intent": "buy_decision",
  "ticker": "NVDA"
}
```

---

## Finance Supervisor Agent

The central autonomous agent.

Responsibilities:

* Determine missing information
* Select relevant skills
* Execute skills dynamically
* Decide when enough information has been gathered
* Generate recommendations

---

## Reflection Agent

Implements the Observe → Think → Act loop.

Example:

```json
{
  "enough_information": false,
  "next_skill": "financial_health_skill"
}
```

---

## Report Agent

Generates professional equity research reports.

---

# 🧩 Agent Skills

### 📈 Stock Price Skill

* Current Price
* Previous Close

Source:

* yFinance

---

### 📊 Market Metrics Skill

* Market Cap
* P/E Ratio
* Beta
* Sector

---

### 💰 Financial Health Skill

* Revenue
* Net Income
* Profit Margin
* Return on Equity
* Debt-to-Equity

---

### 📉 Technical Analysis Skill

* SMA50
* SMA200
* Trend Detection

---

### 📰 News Fetch Skill

* Company News
* Market Updates

---

### 😊 News Sentiment Skill

* Positive
* Neutral
* Negative

Sentiment Classification

---

### ⚠️ Risk Analysis Skill

* Volatility
* Beta Risk
* Financial Risk

---

# 🔄 Autonomous Workflow

Example Query:

```text
Should I invest $10,000 in NVDA for the next 5 years?
```

Execution:

```text
Router

↓

Reflection

↓

Stock Price Skill

↓

Reflection

↓

Financial Health Skill

↓

Reflection

↓

News Sentiment Skill

↓

Reflection

↓

Risk Analysis Skill

↓

Reflection

↓

Enough Information

↓

Recommendation

↓

PDF Report
```

---

# 📄 Output

The system generates:

* Investment Recommendation
* Confidence Score
* Explainable Analysis
* Professional PDF Report

Example:

```text
Recommendation: BUY

Confidence: 84%
```

---

# 🛠️ Tech Stack

### AI

* LangGraph
* LangChain
* Gemini 2.5 Flash

### Data Sources

* yFinance
* News APIs

### Backend

* Python
* Pydantic

### Reporting

* ReportLab

---

# 📂 Project Structure

```text
AI_FINANCE_ANALYST

agents/
├── router_agent.py
├── finance_supervisor_agent.py
├── reflection_agent.py
├── report_agent.py

graph/
├── workflow.py
├── skill_executor.py

skills/
├── stock_price_skill.py
├── market_metrics_skill.py
├── financial_health_skill.py
├── technical_analysis_skill.py
├── news_fetch_skill.py
├── news_sentiment_skill.py
├── risk_analysis_skill.py
├── investment_summary_skill.py
├── pdf_report_skill.py

schemas/
├── router_schema.py
├── reflection_schema.py

state/
├── finance_state.py

main.py
llm.py
```

---

# 🔮 Future Enhancements

* Multi-Stock Comparison
* Portfolio Construction
* Interactive Dashboard
* Real-Time Market Streaming
* Advanced Technical Indicators

---

# 👨‍💻 Author

Jayant Singh Khanna

Computer Engineering Student | Machine Learning Intern | Agentic AI Developer
