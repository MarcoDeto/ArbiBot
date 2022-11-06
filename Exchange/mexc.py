import requests


BASE_URL = 'https://api.mexc.com/api/v3/'


def get_book():
    try:
        response = requests.get(BASE_URL + "ticker/bookTicker")
        response = response.json()
        return response
    except:
        pass

def get_mexc_ticker_value(second_coin):
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