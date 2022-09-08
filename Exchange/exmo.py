import requests


BASE_URL = 'https://api.exmo.com/v1.1/'


def get_book():
    response = requests.get(BASE_URL + "ticker/")
    response = response.json()
    return response
    

def get_exmo_ticker_value(second_coin):

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
    response['ask'] = float(result['buy_price'])
    response['bid'] = float(result['sell_price'])
    return response


def get_symbol(second_coin):
    return second_coin+'USD'