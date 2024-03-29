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

    symbols = get_book()
    if symbols == None or len(symbols) == 0:
        return None
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
    response['ask'] = float(result['ask'][0])
    response['bid'] = float(result['bid'][0])
    return response


def get_symbol(second_coin):
    return second_coin+'/USD'