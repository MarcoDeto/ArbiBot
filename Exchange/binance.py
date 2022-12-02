
# pip install python-binance #OR# py -m pip install python-binance
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
    symbols = get_book()
    if symbols == None or len(symbols) == 0:
        return None
    symbol = get_busd_symbol(second_coin)
    filtered = filter(lambda coin: coin['symbol'] == symbol, symbols)
    try:
        result = list(filtered)[0]
    except:
        symbol = get_usdt_symbol(second_coin)
        filtered = filter(lambda coin: coin['symbol'] == symbol, symbols)
        try:
            result = list(filtered)[0]
        except:
            return None
    
    response = dict()
    response['ask'] = float(result['askPrice'])
    response['bid'] = float(result['bidPrice'])
    return response

def get_busd_symbol(second_coin):
    return second_coin+'BUSD'

def get_usdt_symbol(second_coin):
    return second_coin+'USDT'