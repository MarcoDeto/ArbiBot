import requests


BASE_URL = 'https://api.bittrex.com/v3/'


def get_book():
    response = requests.get(BASE_URL + "markets/tickers")
    response = response.json()
    return response
    

def get_bittrex_ticker_value(second_coin):

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
    response['ask'] = float(result['askRate'])
    response['bid'] = float(result['bidRate'])
    return response


def get_symbol(second_coin):
    return second_coin+'-USD'