import yfinance as yf


def get_stock_info(ticker):

    stock = yf.Ticker(ticker)

    return stock.info


def get_history(
    ticker,
    period="1y"
):

    stock = yf.Ticker(ticker)

    return stock.history(
        period=period
    )