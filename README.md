# Binance Cryptocurrency Trading Bot

This is a Python-based cryptocurrency trading bot that interacts with the **Binance API** to perform automated buy and sell actions for the `LUNAUSDT` trading pair. The bot monitors price changes and executes trades based on simple conditions.

## 🚀 Project Overview

- **Objective**: Automate cryptocurrency trading based on price changes.
- **Asset Traded**: `LUNAUSDT` (LUNA against USDT).
- **Trade Quantity**: 5 units of the asset per order.
- **Strategy**: The bot buys when the price increases compared to the previous price and sells when a specific condition is met (e.g., price increase or a 5% loss).

## 🛠️ Features

- Fetches live market data from Binance using the API.
- Places buy orders based on price increase.
- Sells when conditions (price threshold or loss) are met.
- Uses the `keyboard` library to listen for the "space" key to stop the script.

## 📁 Repository Structure

```plaintext
├── Automated_Trading.py            # Main script for trading
└── README.md                       # Project documentation
```

## 🔧 Prerequisites
Before you begin, ensure you have the following installed:

- Python 3.x
- Binance account and API keys (for live trading).

## Install Dependencies
1. Clone the repository:
```bash
git clone https://github.com/Siddharth-Chandel/binance-trading-bot.git
cd binance-trading-bot
```

2. Ensure you have a `.env` file with your Binance API keys:
```env
Binance_Key=YOUR_API_KEY
Binance_secret_key=YOUR_SECRET_KEY
```

## Dependencies
The bot relies on the following Python libraries:
- `binance`: For interacting with the Binance API.
- `pandas`: For handling and processing data.
- `keyboard`: For listening to user input (e.g., to stop the script).
- `os`: For reading environment variables.
  
Install these using:
```bash
pip install binance pandas keyboard
```

## 🏃‍♂️ How to Run
1. Set your API keys as environment variables or create a `.env` file with the following format:
```env
Binance_Key=YOUR_API_KEY
Binance_secret_key=YOUR_SECRET_KEY
```

2. Run the script:
```bash
python Automated_trading.py
```

3.The bot will continuously monitor the market for price changes and perform buy/sell actions until the "space" key is pressed to stop the script.

## 📊 How it Works
1. **Fetching Market Data**: The bot uses the `getData()` function to fetch historical market data for the `LUNAUSDT` asset.

2. **Buying Logic**: The bot compares the current price with the previous price. If the price increases, it triggers the buy order.

3. **Selling Logic**: If the price increases beyond the buy price or drops by a specified percentage, the bot executes a sell order.

4. **Stop Execution**: Press the "space" key at any time to stop the bot.

## 🤖 Example Output
```bash
2024-12-18 12:00:05,123 - INFO - Buying Successful...
Buying price : 10.50
Last rate = 10.45

2024-12-18 12:01:10,456 - INFO - Selling Successful...
Buying price : 10.50
Selling price : 10.75
Profit % = 2.38
```

## ⚠️ Disclaimer
- **Real Trading**: The bot can be used for real trading, but USE AT YOUR OWN RISK. Make sure to thoroughly test the strategy before deploying it with real funds.
- **Backtesting**: It is recommended to backtest this strategy using historical data before using it for live trading.
- **Security**: Keep your API keys secure. Avoid hardcoding sensitive data into the script.

## 🤝 Contributions
Contributions are welcome! Feel free to fork the repository and submit pull requests for improvements or additional features.

## 📬 Contact
Siddharth Chandel
- Email: siddharthchandel2004@gmail.com
- LinkedIn: [Siddharth Chandel](https://www.linkedin.com/in/siddharth-chandel-001097245/)
