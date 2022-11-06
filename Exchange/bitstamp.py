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
    result = None
    symbols = get_book()
    if symbols == None or len(symbols) == 0:
        return None
    for item in symbols:
        if item['pair'] == second_coin+'/USD':
            result = item
    if result == None:
        return None
    
    response = dict()
    if result['ask'] != None and result['bid'] != None:
        response['ask'] = float(result['ask'])
        response['bid'] = float(result['bid'])
        return response
    else:
        return None