from config import *


def get_best_bid_exchange(binance, cryptocom, mexc):
    list = []
    exchange_list = []
    for exchange in EXCHANGE_LIST:
        exchange_list.append(exchange)

    if binance != None: list.append(binance['bid'])
    else: exchange_list.remove('BINANCE')

    if cryptocom != None: list.append(cryptocom['bid'])
    else: exchange_list.remove('CRYPTO.COM')
        
    if mexc != None: list.append(mexc['bid'])
    else: exchange_list.remove('MEXC')

    try:
        index = list.index(0.0)
        list.remove(0.0)
        exchange_list.remove(exchange_list[index])
    except:
        pass

    value = max(list)
    index = list.index(value)
    response = dict()
    response['name'] = exchange_list[index]
    response['price'] = value
    return response


def get_best_ask_exchange(binance, cryptocom, mexc):
    list = []
    exchange_list = []
    for exchange in EXCHANGE_LIST:
        exchange_list.append(exchange)

    if binance != None: list.append(binance['ask'])
    else: exchange_list.remove('BINANCE')

    if cryptocom != None: list.append(cryptocom['ask'])
    else: exchange_list.remove('CRYPTO.COM')

    if mexc != None: list.append(mexc['ask'])
    else: exchange_list.remove('MEXC')

    try:
        index = list.index(0.0)
        list.remove(0.0)
        exchange_list.remove(exchange_list[index])
    except:
        pass

    value = min(list)
    index = list.index(value)
    response = dict()
    response['name'] = exchange_list[index]
    response['price'] = value
    return response


def get_diff_percent(Xi, Xf):
    percent = ((float(Xf) - float(Xi)) / float(Xi)) * 100
    return round(percent, 3)


def get_symbol(second_coin):
    return second_coin+'_USD'


def prices_to_list(prices):
    list = []
    for AMOUNT in AMOUNT_LIST:
        try: 
            list.append(prices[AMOUNT])
        except:
            continue
    return list


def get_smallest_ask(ask_prices):
    list = prices_to_list(ask_prices)
    smallest = min(list)
    index = list.index(smallest)
    response = dict()
    response['amount'] = int(AMOUNT_LIST[index])
    response['price'] = smallest
    return response


def get_biggest_bid(bid_prices):
    list = prices_to_list(bid_prices)
    biggest = max(list)
    index = list.index(biggest)
    response = dict()
    response['amount'] = int(AMOUNT_LIST[index])
    response['price'] = biggest
    return response