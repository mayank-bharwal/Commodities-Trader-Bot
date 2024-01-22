# EconoMystic: Commodity Trading Bot


This repository contains the source code for a Commodity Trading Bot, specifically designed to trade Gold Futures (CL=F). The bot utilizes a custom algorithm to make trading decisions and tracks its performance over time.

## Features

- **Automated Trading**: The bot makes trading decisions based on the implemented algorithm.
- **Real-time Tracking**: A continuous update mechanism for tracking trading decisions and returns.
- **Visualization**: An integrated visualization tool to graphically represent the trading bot's performance.

## Components

- `CommodityTrader`: A class that encapsulates the trading logic for commodities.
- `Visualizer`: A module to create graph data for visualizing the bot's performance.
- `Flask App`: A web application to display the trading data and graph.

## Setup

1. **Clone the Repository**
   ```
   git clone https://github.com/mayank-bharwal/EconoMystic.git
   cd economystic
   ```

2. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

3. **Run the Bot**
   ```
   python app.py
   ```


### Features

- **Historical Data Analysis**: Utilizes the `yfinance` library to fetch historical data of a specified commodity.
- **Machine Learning Integration**: Incorporates a Logistic Regression model from `sklearn` to predict future price movements.
- **Real-Time Decision Making**: Makes trading decisions based on real-time prices fetched from an external source.

### Methods

- `_get_historical_data()`: Fetches historical price data for the commodity and prepares it for the model.
- `_train_model()`: Trains the logistic regression model on historical data and evaluates its accuracy.
- `make_decision()`: Makes a buy or sell decision based on the current price prediction by the model.


### Dependencies

- `sklearn`: For machine learning model implementation and evaluation.
- `yfinance`: To fetch historical commodity data.
- `pandas` and `numpy`: For data manipulation and numerical operations.

### Example Output

Running the script will output the model's accuracy on the historical data and the current trading decision, either "Buy" or "Sell".

### Integration

This class is designed to be integrated into the broader commodity trading bot system, working in tandem with other components like the data visualization and web interface provided by the Flask app.


## Usage

- **Starting the Bot**: Upon running `app.py`, the bot starts trading and updating the trading history every minute.
- **Web Interface**: Access the bot's web interface at `http://localhost:5000` to view the trading history and performance graph.
- **API Endpoint**: The `/graph-data` endpoint provides the data for the graph in JSON format, which can be used for custom integrations.

## Architecture

- **Flask Framework**: Used for creating the web interface and API.
- **Threading**: A separate thread for continuously updating the trading history.
- **Visualization**: Dynamic graph generation based on the bot's performance.

![Screenshot 2024-01-22 at 2 11 20 AM](https://github.com/mayank-bharwal/EconoMystic/assets/119955673/d723820a-c2c4-46cc-a3eb-f799bbd24458)


## Contribution

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under GNU AFFERO GENERAL PUBLIC LICENSE [](LICENSE).

## Disclaimer

This trading bot is for educational and demonstration purposes only. The trading decisions and return values are simulated and do not guarantee real-world trading success. Use it at your own risk.

Mayank Bharwal

**Happy Trading!** 📈🤖
