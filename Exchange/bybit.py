from datetime import datetime
import hmac
import time
from urllib.parse import quote_plus
from pybit import usdt_perpetual, inverse_perpetual
import requests
import urllib3

TEST_BASE_URL = "https://api-testnet.bybit.com"
TEST_BYBIT_API_KEY = 'rm7rMjCwal2grnNQ54'
TEST_BYBIT_API_SECRET = 'U1sqmmLhaH0Xjp7I0T9K75yJ3m6AnCP1GO6F'

session_unauth = usdt_perpetual.HTTP(
    endpoint = TEST_BASE_URL
)

session_auth = usdt_perpetual.HTTP(
    endpoint = TEST_BASE_URL,
    api_key = TEST_BYBIT_API_KEY,
    api_secret = TEST_BYBIT_API_SECRET
)


def get_bybit_symbols():
    url = TEST_BASE_URL + "/derivatives/v3/public/instruments-info"
    parameters = {
        "category": "linear"
    }
    response = requests.get(url, params=parameters)
    if response.status_code == 200:
        print("sucessfully fetched the data")
        return response.json()['result']['list']
    else:
        print(f"Hello person, there's a {response.status_code} error with your request")


def klines(symbol, interval):
    time_frame = get_bybit_interval(interval)
    now = datetime.now()
    timestamp = int(datetime.timestamp(now))
    return session_unauth.query_kline(
        symbol = symbol,
        interval = time_frame,
        limit = 200,
        from_time = timestamp - 2000
    )['result']


def mark_price_klines(symbol):
    now = datetime.now()
    timestamp = int(datetime.timestamp(now))
    session_unauth = usdt_perpetual.HTTP(
        endpoint="https://api-testnet.bybit.com"
    )
    print(session_unauth.query_mark_price_kline(
        symbol="BTCUSDT",
        interval=1,
        limit=2,
        from_time=1581231260
    ))
    return session_unauth.query_mark_price_kline(
        symbol = 'BTCUSDT',
        interval = 1,
        limit = 200,
        from_time = timestamp - 2000
    )['result']


def get_bybit_price(symbol):
    klines = mark_price_klines(symbol)
    return klines[-1]['close']


def get_wallet_balance():
    response = session_auth.get_wallet_balance()
    ADA = response['result']['ADA']
    BIT = response['result']['BIT']
    BTC = response['result']['BTC']
    DOT = response['result']['DOT']
    EOS = response['result']['EOS']
    ETH = response['result']['ETH']
    LTC = response['result']['LTC']
    LUNA = response['result']['LUNA']
    MANA = response['result']['MANA']
    SOL = response['result']['SOL']
    USDT = response['result']['USDT']
    XRP = response['result']['XRP']
    return (ADA, BIT, BTC, DOT, EOS, ETH, LTC, LUNA, MANA, SOL, USDT, XRP)


def get_usdt_balance():
    response = session_auth.get_wallet_balance()
    USDT = response['result']['USDT']
    return USDT['available_balance']


def get_order_quantity(symbol):
    usdt = get_usdt_balance()
    usdt_quantity = (usdt * 3) / 100
    price = get_bybit_price(symbol)
    return round(usdt_quantity / price, 3)


def place_order(symbol, take_profit, stop_loss, quantity):
    return session_auth.place_active_order(
        symbol = symbol,
        side = "Buy",
        order_type = "Market",
        qty = quantity,
        reduce_only = False,
        close_on_trigger = False,
        time_in_force = "GoodTillCancel",
        take_profit = take_profit,
        stop_loss = stop_loss,
    )['result']


def get_active_orders(symbol):
    return session_auth.get_active_order(
        symbol = symbol
    )['result']


def close_order(symbol, quantity):
    return session_auth.place_active_order(
        symbol = symbol,
        side = "Buy",
        order_type = "Market",
        qty = quantity,
        reduce_only = True,
        close_on_trigger = True,
        time_in_force = "GoodTillCancel",
    )['result']

session_auth = usdt_perpetual.HTTP(
    endpoint="https://api-testnet.bybit.com",
    api_key="your api key",
    api_secret="your api secret"
)
print(session_auth.get_active_order(
    symbol="BTCUSDT"
))

def open_bybit_order(symbol, take_profit, stop_loss):
    quantity = get_order_quantity(symbol)
    print('\n'+str(quantity)+'\n')
    order_placed = place_order(symbol, take_profit, stop_loss, quantity)
    print('\n'+str(order_placed)+'\n')
    return order_placed


def close_bybit_order(symbol, quantity):

    order_closed = close_order(symbol, quantity)


def get_bybit_interval(interval):
    match (interval):
        case '1m': return 1
        case '3m': return 3
        case '5m': return 5
        case '15m': return 15
        case '30m': return 30
        case '1h': return 60
        case '2h': return 120
        case '4h': return 240
        case '6h': return 360
        case '12h': return 720
        case '1d': return 'D'
        case '1w': return 'W'
        case '1M': return 'M'
        case _: return None


def auth(url):
    timestamp = int(time.time() * 10 ** 3)
    headers = {}
    params = {  # delete order request
        "orderId": "1084090149712726016",
        "api_key": TEST_BYBIT_API_KEY,
        "timestamp": str(timestamp),
        "recv_window": "5000"
    }
    param_str = ''
    for key in sorted(params.keys()):
        v = params[key]
        if isinstance(params[key], bool):
            if params[key]:
                v = "true"
            else:
                v = "false"
        param_str += key + "=" + v + "&"
    param_str = param_str[:-1]
    signature = str(hmac.new(
        bytes(TEST_BYBIT_API_SECRET, "utf-8"),
        bytes(param_str, "utf-8"), digestmod="sha256"
    ).hexdigest())
    sign_real = {
        "sign": signature
    }
    param_str = quote_plus(param_str, safe="=&")
    full_param_str = f"{param_str}&sign={sign_real['sign']}"
    urllib3.disable_warnings()
    #url = "https://api.bybit.com/spot/v1/order"
    return f"{url}?{full_param_str}"


def main():
    symbol = 'BTCUSDT'
    take_profit = 50000
    stop_loss = 20000

    order_placed = open_bybit_order(symbol, take_profit, stop_loss)
    time.sleep(1)

    orders = get_active_orders(symbol)
    print('\n'+str(orders)+'\n')
    time.sleep(1)

    order_id = order_placed['order_id']
    user_id = order_placed['user_id']
    order_link_id =  ''

    order_closed = close_order(symbol, quantity)

    
    orders = get_active_orders(symbol)
    print('\n'+str(orders)+'\n')
    time.sleep(1)


main()


class Coin_Balance:
    def __init__(self, equity, available_balance, used_margin, order_margin,
                 position_margin, occ_closing_fee, occ_funding_fee, wallet_balance,
                 realised_pnl, unrealised_pnl, cum_realised_pnl, given_cash, service_cash):

        self.equity = equity
        self.available_balance = available_balance
        self.used_margin = used_margin
        self.order_margin = order_margin
        self.position_margin = position_margin
        self.occ_closing_fee = occ_closing_fee
        self.occ_funding_fee = occ_funding_fee
        self.wallet_balance = wallet_balance
        self.realised_pnl = realised_pnl
        self.unrealised_pnl = unrealised_pnl
        self.cum_realised_pnl = cum_realised_pnl
        self.given_cash = given_cash
        self.service_cash = service_cash
