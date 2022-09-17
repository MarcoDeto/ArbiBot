import requests


BASE_URL = 'https://www.bitstamp.net/api/v2/'


def get_book():
    try:
        response = requests.get(BASE_URL + "ticker/")
        response = response.json()
        return response
    except:
        pass

def get_bitstamp_ticker_value(second_coin):

    symbols = get_book()
    filtered = filter(lambda coin: coin['symbol'] == second_coin+'/USD', symbols)
    try:
        result = list(filtered)[0]
    except:
        filtered = filter(lambda coin: coin['i'] == second_coin+'/EUR', symbols)
        try:
            result = list(filtered)[0]
        except:
            return None
    
    response = dict()
    response['ask'] = float(result['ask'])
    response['bid'] = float(result['bid'])
    return response