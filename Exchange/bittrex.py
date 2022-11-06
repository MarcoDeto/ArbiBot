import requests


BASE_URL = 'https://api.bittrex.com/v3/'


def get_book():
    try:
        response = requests.get(BASE_URL + "markets/tickers")
        response = response.json()
        return response
    except:
        pass

def get_bittrex_ticker_value(second_coin):
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
    if result['askRate'] != None and result['bidRate'] != None:
        response['ask'] = float(result['askRate'])
        response['bid'] = float(result['bidRate'])
        return response
    else:
        return None


def get_symbol(second_coin):
    return second_coin+'-USD'