import yfinance as yf

def get_realtime_price(ticker):
    """
    Fetches the real-time price of a given commodity.
    
    :param ticker: The ticker symbol of the commodity.
    :return: Real-time price.
    """
    commodity = yf.Ticker(ticker)
    data = commodity.history(period="1d", interval="1m")
    latest_price = data['Close'].iloc[-1]
    return latest_price

# Example usage
if __name__ == "__main__":
    ticker = "CL=F"  # Gold futures ticker symbol
    price = get_realtime_price(ticker)
    print(f"Real-time price of {ticker}: {price}")
