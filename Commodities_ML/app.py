from flask import Flask, render_template, jsonify
from trader import CommodityTrader
from visualizer import create_graph_data
import threading
import time
import random
app = Flask(__name__)
trader = CommodityTrader("CL=F")  # Gold futures

# This list will store the trading decisions and returns for visualization
trading_history = []

def update_trading_history():
    """
    Continuously updates trading history every minute.
    """
    while True:
        decision = trader.make_decision()
        # Here, you would also add logic to calculate returns
        # For example, let's just use a random return value
        # In a real application, this would be based on the trade outcome
        return_value = random.uniform(-5, 5)  # Example return value
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        trading_history.append((timestamp, decision, return_value))
        time.sleep(60)  # Update every minute

@app.route('/graph-data')
def graph_data():
    graph_trace = create_graph_data(trading_history)
    return jsonify(graph_trace)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    threading.Thread(target=update_trading_history, daemon=True).start()
    app.run(debug=True)
