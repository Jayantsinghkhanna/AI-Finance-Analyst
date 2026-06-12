import ta


def calculate_rsi(df):

    return ta.momentum.RSIIndicator(
        close=df["Close"]
    ).rsi().iloc[-1]