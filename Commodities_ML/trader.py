from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import yfinance as yf
import pandas as pd
import numpy as np
from data_fetcher import get_realtime_price

class CommodityTrader:
    def __init__(self, ticker):
        self.ticker = ticker
        self.model = LogisticRegression()
        self._train_model()

    def _get_historical_data(self):
        """
        Fetches historical data for the commodity.
        """
        data = yf.download(self.ticker, start="2020-01-01", end="2023-01-01")
        data['Target'] = np.where(data['Close'].shift(-1) > data['Close'], 1, 0)
        return data

    def _train_model(self):
        """
        Trains the logistic regression model.
        """
        data = self._get_historical_data()
        X = data[['Open', 'High', 'Low', 'Close']].values
        y = data['Target'].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        print(f"Model accuracy: {accuracy_score(y_test, predictions)}")

    def make_decision(self):
        """
        Makes a trading decision based on the current price.
        """
        current_price = get_realtime_price(self.ticker)
        prediction = self.model.predict([[current_price, current_price, current_price, current_price]])
        return "Buy" if prediction[0] == 1 else "Sell"

# Example usage
if __name__ == "__main__":
    trader = CommodityTrader("GC=F")  # Gold futures
    decision = trader.make_decision()
    print(f"Trading decision for {trader.ticker}: {decision}")
