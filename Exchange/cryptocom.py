
import hmac
import hashlib
import time

import requests

BASE_URL = 'https://api.crypto.com/v2/'
API_KEY = "TbjeFj1g8kuFv6h1gRNNCk"
SECRET_KEY = "wSCrbsQGtB8jpppeEvh1NJ"

req = {
    "id": 14,
    "method": "private/create-order-list",
    "api_key": API_KEY,
    "params": {
        "contingency_type": "OCO",
        "order_list": [
            {
                "instrument_name": "ONE_USDT",
                "side": "BUY",
                "type": "LIMIT",
                "price": "0.24",
                "quantity": "1.0"
            },
            {
                "instrument_name": "ONE_USDT",
                "side": "BUY",
                "type": "STOP_LIMIT",
                "price": "0.27",
                "quantity": "1.0",
                "trigger_price": "0.26"
            }
        ]
    },
    "nonce": int(time.time() * 1000)
}

# First ensure the params are alphabetically sorted by key
param_str = ""

MAX_LEVEL = 3


def get_book():
    response = requests.get(BASE_URL + "public/get-book?instrument_name=VVS_USDT")
    response = response.json()['result']
    return response


def get_symbols():
    response = requests.get(BASE_URL + "public/get-ticker")
    response = response.json()['result']
    return response['data']
    

def get_ticker_value(symbol):
    '''
    Name	Type       Description
     i     number      Instrument Name, e.g. BTC_USDT, ETH_CRO, etc.
     b     number      The current best bid price, null if there aren't any bids
     k     number      The current best ask price, null if there aren't any asks
     a     number      The price of the latest trade, null if there weren't any trades
     t     number      Timestamp of the data
     v     number      The total 24h traded volume
     h     number      Price of the 24h highest trade
     l     number      Price of the 24h lowest trade, null if there weren't any trades
     c     number      24-hour price change, null if there weren't any trades

    '''
    symbols = get_symbols()
    filtered = filter(lambda coin: coin['i'] == symbol, symbols)
    try:
        result = list(filtered)[0]
    except:
        return None
    
    response = dict()
    response['ask'] = result['k']
    response['bid'] = result['b']
    return response


def params_to_str(obj, level):
    if level >= MAX_LEVEL:
        return str(obj)

    return_str = ""
    for key in sorted(obj):
        return_str += key
        if isinstance(obj[key], list):
            for subObj in obj[key]:
                return_str += params_to_str(subObj, ++level)
        else:
            return_str += str(obj[key])
    return return_str


if "params" in req:
    param_str = params_to_str(req['params'], 0)

payload_str = req['method'] + \
    str(req['id']) + req['api_key'] + param_str + str(req['nonce'])

req['sig'] = hmac.new(
    bytes(str(SECRET_KEY), 'utf-8'),
    msg=bytes(payload_str, 'utf-8'),
    digestmod=hashlib.sha256
).hexdigest()


get_book()