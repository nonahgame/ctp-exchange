import pandas as pd
from binance.client import Client
from config import API_KEY, API_SECRET, SYMBOL, INTERVAL

client = Client(API_KEY, API_SECRET)

def fetch_ohlcv(symbol=SYMBOL, interval=INTERVAL, limit=10):
    klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)
    df = pd.DataFrame(klines, columns=[
        'timestamp', 'open', 'high', 'low', 'close',
        'volume', 'close_time', 'quote_asset_volume',
        'number_of_trades', 'taker_buy_base_vol', 'taker_buy_quote_vol', 'ignore'
    ])
    df['open'] = df['open'].astype(float)
    df['close'] = df['close'].astype(float)
    return df[['open', 'close']]

def check_signal(df):
    last_row = df.iloc[-1]
    if last_row['close'] > last_row['open']:
        return 'BUY'
    elif last_row['close'] < last_row['open']:
        return 'SELL'
    else:
        return 'HOLD'

def place_order(signal, quantity=0.00011):
    if signal == 'BUY':
        return client.order_market_buy(symbol=SYMBOL, quantity=quantity)
    elif signal == 'SELL':
        return client.order_market_sell(symbol=SYMBOL, quantity=quantity)
    return None
