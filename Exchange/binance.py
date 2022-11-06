from binance.client import Client
from config import *


client = Client(BINANCE_API_KEY, BINANCE_API_SECRET, testnet=False)


def get_book():
    try:
        response = client.get_orderbook_tickers()
        return response
    except:
        pass
    

def get_binance_ticker_value(second_coin):
    result = None
    symbols = get_book()
    if symbols == None or len(symbols) == 0:
        return None
    symbol = get_symbol(second_coin)
    for item in symbols:
        if item['symbol'] == symbol+'C' or item['symbol'] == symbol+'T' :
            result = item
    if result == None:
        return None
    
    response = dict()
    if result['askPrice'] != None and result['bidPrice'] != None:
        response['ask'] = float(result['askPrice'])
        response['bid'] = float(result['bidPrice'])
        return response
    else:
        return None


def get_symbol(second_coin):
    return second_coin+'USD'