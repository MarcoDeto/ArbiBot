from config import *


def get_best_bid_exchange(ascendex, binance, bitstamp, bittrex, cryptocom, exmo, gateio, mexc):
    list = []
    exchange_list = []
    for exchange in EXCHANGE_LIST:
        exchange_list.append(exchange)

    if ascendex != None: list.append(float(ascendex['bid']))
    else: exchange_list.remove('ASCENDEX')

    if binance != None: list.append(float(binance['bid']))
    else: exchange_list.remove('BINANCE')

    if bitstamp != None: list.append(float(bitstamp['bid']))
    else: exchange_list.remove('BITSTAMP')

    if bittrex != None: list.append(float(bittrex['bid']))
    else: exchange_list.remove('BITTREX')

    if cryptocom != None: list.append(float(cryptocom['bid']))
    else: exchange_list.remove('CRYPTO.COM')

    if exmo != None: list.append(float(exmo['bid']))
    else: exchange_list.remove('EXMO')

    if gateio != None: list.append(float(gateio['bid']))
    else: exchange_list.remove('GATEIO')
        
    if mexc != None: list.append(float(mexc['bid']))
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
    response['price'] = float(value)
    return response


def get_best_ask_exchange(ascendex, binance, bitstamp, bittrex, cryptocom, exmo, gateio, mexc):
    list = []
    exchange_list = []
    for exchange in EXCHANGE_LIST:
        exchange_list.append(exchange)

    if ascendex != None: list.append(float(ascendex['ask']))
    else: exchange_list.remove('ASCENDEX')

    if binance != None: list.append(float(binance['ask']))
    else: exchange_list.remove('BINANCE')

    if bitstamp != None: list.append(float(bitstamp['ask']))
    else: exchange_list.remove('BITSTAMP')

    if bittrex != None: list.append(float(bittrex['ask']))
    else: exchange_list.remove('BITTREX')

    if cryptocom != None: list.append(float(cryptocom['ask']))
    else: exchange_list.remove('CRYPTO.COM')

    if exmo != None: list.append(float(exmo['ask']))
    else: exchange_list.remove('EXMO')

    if gateio != None: list.append(float(gateio['ask']))
    else: exchange_list.remove('GATEIO')
        
    if mexc != None: list.append(float(mexc['ask']))
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
    response['price'] = float(value)
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
            list.append(float(prices[AMOUNT]))
        except:
            continue
    return list


def get_smallest_ask(ask_prices):
    list = prices_to_list(ask_prices)
    smallest = min(list)
    index = list.index(smallest)
    response = dict()
    response['amount'] = int(AMOUNT_LIST[index])
    response['price'] = float(smallest)
    return response


def get_biggest_bid(bid_prices):
    list = prices_to_list(bid_prices)
    biggest = max(list)
    index = list.index(biggest)
    response = dict()
    response['amount'] = int(AMOUNT_LIST[index])
    response['price'] = float(biggest)
    return response