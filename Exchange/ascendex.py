import requests


BASE_URL = 'https://ascendex.com/api/pro/v1/'


def get_book():
    try:
        response = requests.get(BASE_URL + "spot/ticker")
        response = response.json()
        return response
    except:
        pass
    

def get_ascendex_ticker_value(second_coin):
    result = None
    symbols = get_book()
    if symbols == None or len(symbols) == 0:
        return None
    symbol = get_symbol(second_coin)
    for item in symbols['data']:
        if item['symbol'] == symbol+'C' or item['symbol'] == symbol+'T' :
            result = item
    if result == None:
        return None
    
    response = dict()
    if result['ask'][0] != None and result['bid'][0] != None:
        response['ask'] = float(result['ask'][0])
        response['bid'] = float(result['bid'][0])
        return response
    else:
        return None


def get_symbol(second_coin):
    return second_coin+'/USD'