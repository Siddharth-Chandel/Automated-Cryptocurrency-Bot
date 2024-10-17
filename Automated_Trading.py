from time import sleep
from binance import Client, exceptions
import pandas as pd
from keyboard import is_pressed
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Binance Details
key = os.getenv('Binance_Key')
secret_key = os.getenv('Binance_secret_key')

client = Client(key, secret_key)

# Coin Details
asset = "LUNAUSDT"
qty = 5.0

# Getting the live price of the asset and append it in a list
data_list = ['0']

def getData(symbol, interval, lookback):
    """Retrieve historical klines data."""
    try:
        df = pd.DataFrame(client.get_historical_klines(
            symbol=symbol, interval=interval, start_str=lookback+" UTC + 5:30"))
        df = df.iloc[:, :6]
        df.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
        df.set_index('Time', inplace=True)
        df.index = pd.to_datetime(df.index, unit='ms')
        df = df.astype(float)
        return df
    except exceptions.BinanceAPIException as e:
        logging.error(f"Error fetching data: {e}")
        return None

def buy():
    """Place a buy order."""
    try:
        avg = client.get_orderbook_ticker(symbol=asset)
        # Uncomment the following lines to place a real order
        # client.create_order(symbol=asset, side="BUY",
        #                     type="LIMIT",
        #                     timeInForce='GTC',
        #                     price=avg['askPrice'],
        #                     quantity=qty)
        return avg['askPrice']
    except exceptions.BinanceAPIException as e:
        logging.error(f"Error placing buy order: {e}")
        return None

def buyAgain():
    """Loop for buying based on price changes."""
    global data_list, buyc
    while not is_pressed('space'):
        data = getData(asset, '1m', '120m')
        if data is not None:
            current_price = str(data.iloc[-1].Close)
            if data_list[0] < current_price:
                logging.info(f"Buying Successful...\nBuying price : {current_price}\nLast rate = {data_list[0]}\n")
                buyc = buy()
                break
            else:
                logging.info(f"Current Price : {current_price}, Previous Price : {data_list[0]}")
                data_list[0] = current_price
        sleep(1)
    sleep(3)
    sell()

def sell():
    """Loop for selling based on price changes."""
    global data_list
    while not is_pressed('space'):
        data = getData(asset, '1m', '120m')
        if data is not None:
            current_price = data.iloc[-1].Close
            difference = float(current_price) - float(buyc)
            if current_price > float(buyc):
                if data_list[0] > str(current_price):
                    bid = client.get_orderbook_ticker(symbol=asset)
                    # Uncomment the following lines to place a real order
                    # client.futures_create_order(symbol=asset, side="SELL",
                    #                             type="LIMIT",
                    #                             timeInForce='GTC',
                    #                             price=bid['bidPrice'],
                    #                             quantity=qty)
                    pricex = bid['bidPrice']
                    logging.info(f"\nSelling Successful...\nBuying price : {buyc}\nSelling price : {pricex}\nLast rate = {data_list[0]}\nProfit % = {(float(pricex)-float(buyc))/float(buyc)*100}")
                    data_list[0] = pricex
                    break
                else:
                    logging.info(f"Price is higher now. Current Price : {current_price}, Buy at price = {buyc}, Difference : {difference}")
                    data_list[0] = str(current_price)
            else:
                if difference <= -5:
                    bid = client.get_orderbook_ticker(symbol=asset)
                    # Uncomment the following lines to place a real order
                    # client.futures_create_order(symbol=asset, side="SELL",
                    #                             type="LIMIT",
                    #                             timeInForce='GTC',
                    #                             price=bid['bidPrice'],
                    #                             quantity=qty)
                    pricex = bid['bidPrice']
                    logging.info(f"\nSelling Successful...\nBuying price : {buyc}\nSelling price : {pricex}\nLast rate = {data_list[0]}\nProfit % = {(float(pricex)-float(buyc))/float(buyc)*100}")
                    data_list[0] = pricex
                else:
                    logging.info(f'Price is lower than the buying price. Current Price : {current_price}, Buy at price = {buyc}, Difference : {difference}')
                    data_list[0] = '0'
        sleep(1)
    sleep(3)
    buyAgain()

if __name__ == '__main__':
    buyc = buy()
    sleep(3)
    sell()
