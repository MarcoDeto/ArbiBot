import requests


BASE_URL = 'https://api.gateio.ws/api/v4/'


def get_book():
    try:
        response = requests.get(BASE_URL + "spot/tickers/")
        response = response.json()
        return response
    except:
        pass
    

def get_gateio_ticker_value(second_coin):
    '''
        "currency_pair": "BTC_USDT",
        "last": "2.46140352",
        "lowest_ask": "2.477",
        "highest_bid": "2.4606821",
        "change_percentage": "-8.91",
        "change_utc0": "-8.91",
        "change_utc8": "-8.91",
        "base_volume": "656614.0845820589",
        "quote_volume": "1602221.66468375534639404191",
        "high_24h": "2.7431",
        "low_24h": "1.9863",
        "etf_net_value": "2.46316141",
        "etf_pre_net_value": "2.43201848",
        "etf_pre_timestamp": 1611244800,
        "etf_leverage": "2.2803019447281203"
    '''
    symbols = get_book()
    symbol = get_symbol(second_coin)
    filtered = filter(lambda coin: coin['currency_pair'] == symbol+'C', symbols)
    try:
        result = list(filtered)[0]
    except:
        filtered = filter(lambda coin: coin['i'] == symbol+'T', symbols)
        try:
            result = list(filtered)[0]
        except:
            return None
    
    response = dict()
    response['ask'] = float(result['lowest_ask'])
    response['bid'] = float(result['highest_bid'])
    return response


def get_symbol(second_coin):
    return second_coin+'_USD'

