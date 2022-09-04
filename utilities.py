from config import AMOUNT_LIST

def get_diff_percent(Xi, Xf):
    percent = ((float(Xf) - float(Xi)) / float(Xi)) * 100
    return round(percent, 3)


def get_symbol(second_coin, stable_coin):
    return second_coin+'_'+stable_coin


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