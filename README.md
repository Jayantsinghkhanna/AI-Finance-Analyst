# 🚀 Autonomous Finance Analyst

An Autonomous Finance Analyst built using **LangGraph**, **Agent Skills**, **Gemini**, and **yFinance** that performs live stock analysis, financial health evaluation, technical analysis, news sentiment analysis, risk assessment, investment recommendations, and automated PDF report generation.

---

## 🎯 Project Overview

Traditional LLMs can provide investment opinions but cannot access live market data, evaluate current financial metrics, or perform structured financial analysis.

This project combines:

* Autonomous Agent Workflows
* Agent Skills Architecture
* Live Financial Data
* Financial Reasoning
* Automated Report Generation

to create an AI-powered finance analyst capable of producing professional investment reports.

---

## 🏗️ Architecture

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

Skill Executor

     ├── Stock Price Skill
     ├── Market Metrics Skill
     ├── Financial Health Skill
     ├── Technical Analysis Skill
     ├── News Fetch Skill
     ├── News Sentiment Skill
     ├── Risk Analysis Skill
     └── Investment Summary Skill

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

Investment Report.pdf
```

---

## 🤖 Agent Design

### 1. Router Agent

Uses Gemini + Pydantic Structured Output to:

* Understand user intent
* Extract stock ticker symbols
* Route requests

Example:

```json
{
  "intent": "buy_decision",
  "ticker": "NVDA"
}
```

---

### 2. Finance Supervisor Agent

The core autonomous agent responsible for:

* Planning analysis steps
* Selecting required skills
* Gathering missing information
* Executing financial analysis
* Generating recommendations

The supervisor follows an Observe → Think → Act loop.

---

### 3. Report Agent

Generates a professional equity research report containing:

* Executive Summary
* Market Snapshot
* Financial Health Analysis
* Technical Analysis
* News & Sentiment
* Risk Assessment
* Investment Recommendation
* Confidence Score

---

## 🧩 Agent Skills

### 📈 Stock Price Skill

Fetches:

* Current Price
* Previous Close

Source:

* yFinance

---

### 📊 Market Metrics Skill

Fetches:

* Market Cap
* P/E Ratio
* Beta
* Sector

Source:

* yFinance

---

### 💰 Financial Health Skill

Evaluates:

* Revenue
* Net Income
* Profit Margin
* Return on Equity
* Debt-to-Equity Ratio

---

### 📉 Technical Analysis Skill

Calculates:

* SMA50
* SMA200
* Trend Analysis

---

### 📰 News Fetch Skill

Retrieves:

* Latest company news
* Market developments

---

### 😊 News Sentiment Skill

Performs:

* Sentiment Analysis
* Bullish / Neutral / Bearish Classification

---

### ⚠️ Risk Analysis Skill

Evaluates:

* Volatility
* Beta Risk
* Financial Risk

---

### 📝 Investment Summary Skill

Creates:

* Investment Summary
* Key Insights
* Recommendation Inputs

---

## 🔄 Autonomous Workflow

For a query such as:

```text
Should I invest $10,000 in NVDA for the next 5 years?
```

The system:

1. Detects intent and ticker
2. Retrieves live market data
3. Evaluates company fundamentals
4. Performs technical analysis
5. Analyzes market sentiment
6. Assesses investment risks
7. Generates recommendation
8. Creates a professional report
9. Exports report as PDF

---

## 🛠️ Tech Stack

### AI & Agent Frameworks

* LangGraph
* LangChain
* Google Gemini 2.5 Flash

### Data Sources

* yFinance
* News Search APIs

### Backend

* Python
* Pydantic

### Reporting

* ReportLab

---

## 📂 Project Structure

```text
AI_FINANCE_ANALYST

agents/
│
├── router_agent.py
├── finance_supervisor_agent.py
├── report_agent.py

graph/
│
├── workflow.py
├── skill_executor.py

skills/
│
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
│
├── router_schema.py
├── sentiment_schema.py

tools/
│
├── yfinance_tool.py
├── news_tool.py
├── technical_tool.py

state/
│
├── finance_state.py

main.py
llm.py
```

---

## 💡 Example Queries

### Stock Price

```text
What is the current stock price of AAPL?
```

### News Analysis

```text
What are the latest news updates about Tesla?
```

### Investment Recommendation

```text
Should I invest $10,000 in NVDA for the next 5 years?
```

### Full Analysis

```text
Analyze AMD and tell me whether it is a good investment.
```

---

## 📄 Output

The system generates:

### Recommendation

```text
BUY
HOLD
SELL
```

### Confidence Score

```text
84%
```

### Professional PDF Report

```text
reports/NVDA_Investment_Report.pdf
```

---

## 🔮 Future Enhancements

* Multi-Stock Comparison
* Portfolio Construction
* Interactive Dashboard
* Advanced Technical Indicators
* Real-Time Streaming Market Data
* Portfolio Risk Optimization

---

## 👨‍💻 Author

**Jayant Singh Khanna**

Computer Engineering Student | AI & ML Enthusiast | Agentic AI Developer

Built as an exploration into Autonomous AI Agents, Financial Analysis, and Agent Skills Architecture.
