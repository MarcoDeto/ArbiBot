import time
import asyncio
from binance.client import Client
from config import *

client = Client(BINANCE_API_KEY, BINANCE_API_SECRET, testnet=False)


def get_book():
    response = client.get_orderbook_tickers()
    return response
    

def get_binance_ticker_value(second_coin):
    '''
    Name	Type       Description
     i     number      Instrument Name, e.g. BTC_USDT, ETH_CRO, etc.
     b     number      The current best bid price, null if there aren't any bids
     k     number      The current best ask price, null if there aren't any asks
     a     number      The price of the latest trade, null if there weren't any trades
     t     number      Timestamp of the data
     v     number      The total 24h traded volume
     h     number      Price of the 24h highest trade
     l     number      Price of the 24h lowest trade, null if there weren't any trades
     c     number      24-hour price change, null if there weren't any trades

    '''
    symbols = get_book()
    symbol = get_symbol(second_coin)
    filtered = filter(lambda coin: coin['symbol'] == symbol+'C', symbols)
    try:
        result = list(filtered)[0]
    except:
        filtered = filter(lambda coin: coin['i'] == symbol+'T', symbols)
        try:
            result = list(filtered)[0]
        except:
            return None
    
    response = dict()
    response['ask'] = float(result['askPrice'])
    response['bid'] = float(result['bidPrice'])
    return response


def get_symbol(second_coin):
    return second_coin+'USD'