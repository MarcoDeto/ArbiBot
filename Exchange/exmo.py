import requests


BASE_URL = 'https://api.exmo.com/v1.1/'


def get_book():
    try:
        response = requests.get(BASE_URL + "ticker/")
        response = response.json()
        return response
    except:
        pass
    

def get_exmo_ticker_value(second_coin):
    result = None
    symbols = get_book()
    if symbols == None or len(symbols) == 0:
        return None
    symbol = get_symbol(second_coin)
    
    try:
        result = symbols[symbol]
    except:
        return None
    
    response = dict()
    if result['buy_price'] != None and result['sell_price'] != None:
        response['ask'] = float(result['buy_price'])
        response['bid'] = float(result['sell_price'])
        return response
    else:
        return None


def get_symbol(second_coin):
    return second_coin+'_USD'