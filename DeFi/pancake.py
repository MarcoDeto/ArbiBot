# pip install webdriver-manager #OR# py -m pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Safari, Edge, Chrome  # pip install selenium #OR# py -m pip install selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from Exchange.ascendex import *
from Exchange.binance import *
from Exchange.bitstamp import *
from Exchange.bittrex import *
from Exchange.cryptocom import *
from Exchange.exmo import *
from Exchange.gateio import *
from Exchange.mexc import *

from config import AMOUNT_LIST
from telegram import sendMessage
from utilities import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

coin_basec = 'BUSD'

coin_list = ['BNB', 'ACH', 'ADA', 'ADX', 'ALICE', 'ALPA', 'ALPACA',
             'ALPHA', 'AMPL', 'ANTEX', 'AOG', 'ATOM', 'APE', 'APX', 'APYS', 'ARPA',
             'ARV', 'ASR', 'ATA', 'ATM', 'ATOM', 'AXS', 'BABYCAKE', 'BAKE', 'BAND',
             'BATH', 'BBT', 'BCH', 'BCOIN', 'BDO', 'BELT', 'BETA', 'BETH',
             'BFI', 'BIFI', 'BLK', 'BMON', 'BONDLY', 'BORING', 'BP', 'BRY', 'BSCX', 'BSW',
             'BTCB', 'BTCST', 'BTR', 'BURGER', 'BUX', 'C98', 'CART', 'CEEK',
             'CGG', 'CHESS', 'CHR', 'COMP', 'CREAM', 'CTK', 'CVP', 'CYC',
             'DAI', 'DAR', 'DEGO', 'DERI', 'DEXE', 'DFD', 'DFT', 'DG', 'DITTO', 'DKT', 
             'DODO', 'DOT', 'DPT', 'DUET', 'DUSK', 'DVI', 'EGLD', 'ELON', 'EOS', 
             'EPS', 'ERA', 'ERTHA', 'ETERNAL', 'EZ', 'FIGHT', 'FIL', 'FINE',
             'FORM', 'FRONT', 'FROYO', 'FUEL', 'FUSE', 'GEAR', 'GMEE',
             'GMI', 'GMT', 'GQ', 'GUM', 'HAI', 'HAKKA', 'HAPPY', 'HAY',
             'HGET', 'HIGH', 'HOOK', 'HOOP', 'HTB', 'HTD', 'HZN', 'IDIA', 'IF',
             'INJ', 'INSUR', 'IOTX', 'JASMY', 'JGN', 'JUV', 'KALM', 'KART', 'KRS', 'KTN',
             'KUN', 'LAZIO', 'LIGHT', 'LMT', 'LOA', 'LOOKS', 'LTC',
             'LTO', 'MANA', 'MARSH', 'MASK', 'MATH', 'MBL', 'MBOX', 'MCB', 'MCRN', 'MHUNT',
             'MONI', 'MTRG', 'NABOX', 'NAOS', 'NBT', 'NFT', 'NRV', 'NULS',
             'NVT', 'O3', 'ODDZ', 'OLE', 'ORBS', 'PEAK', 'PEEL',
             'PEOPLE', 'PERL', 'PEX', 'PMON', 'PNT', 'PORTO', 'POTS', 'PRL', 'PROM', 
             'PROS', 'PSG', 'PSTAKE', 'QBT', 'QKC', 'QSD', 'QUIDD', 'RABBIT', 'RACA', 
             'RAMP', 'REEF', 'REVV', 'RFOX', 'RPG', 'SAND', 'SANTOS', 'SDAO', 'SFP', 'SFUND',
             'SHELL', 'SKILL', 'SPARTA', 'SPIN', 'SPS', 'SUSHI', 'SUTER', 'SWAMP', 'SWG', 'SWINGBY',
             'SWTH', 'SXP', 'TEN', 'THG', 'TINC', 'TITAN', 'TKO', 'TLM', 'TLOS', 'TPT',
             'TRIVIA', 'TRX', 'TUSD', 'TWT', 'TXL', 'UBXT', 'UNFI', 'USDC',
             'USDT', 'VAI', 'VET', 'VRT', 'WATCH', 'WBNB', 'WELL', 'WEX', 'WIN', 'WMASS',
             'WMX', 'WOOP', 'WSG', 'WZRD', 'XCAD', 'XCN', 'XCV', 'XED', 'XEND',
             'XMS', 'XRP', 'XTZ', 'XVS', 'XWG', 'YEL', 'YFII', 'ZEC', 'ZEE', 'ZIL', 'ZOO' ]


async def get_pancake_finance(telegram):

    result_list = []

    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--disable-gpu')
    #chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--mute-audio")
    chrome_driver_manager = ChromeDriverManager().install()
    driver = Chrome(service=Service(chrome_driver_manager),chrome_options=chrome_options)

    #driver = Chrome(service=Service(chrome_driver_manager))

    time.sleep(1)
    driver.get('https://pancakeswap.finance/swap')
    time.sleep(3)

    stable_coin = coin_basec
    result = []
    for second_coin in coin_list:
        symbol = get_symbol(second_coin)
        ascendex = get_ascendex_ticker_value(second_coin)
        binance = get_binance_ticker_value(second_coin)
        bitstamp = get_bitstamp_ticker_value(second_coin)
        bittrex = get_bittrex_ticker_value(second_coin)
        cryptocom = get_cryptocom_ticker_value(symbol)
        exmo = get_exmo_ticker_value(second_coin)
        gateio = get_gateio_ticker_value(second_coin)
        mexc = get_mexc_ticker_value(second_coin)
        if binance == None:
            print(symbol)
            continue
        result = dict()
        ask_prices = {}
        bid_prices = {}
        prices = get_price_coin(
            driver, AMOUNT_LIST, stable_coin, second_coin, ask_prices, bid_prices)
        result['coin'] = second_coin
        result['value'] = prices
        result_list.append(result)
        if len(prices['ask']) > 0:
            smallest_ask = get_smallest_ask(prices['ask'])
            ask_exchange = get_best_bid_exchange(ascendex, binance, bitstamp, bittrex, cryptocom, exmo, gateio, mexc)
            if (smallest_ask != None and ask_exchange != None):
                percent = get_diff_percent(smallest_ask['price'], ask_exchange['price'])
                if percent > 0.4:
                    await sendMessage(telegram, symbol, smallest_ask['amount'], smallest_ask['price'], 
                                  ask_exchange['price'], ask_exchange['name'], percent, buy_on_vvs=True)

        if len(prices['bid']) > 0:
            biggest_bid = get_biggest_bid(prices['bid'])
            bid_exchange = get_best_ask_exchange(ascendex, binance, bitstamp, bittrex, cryptocom, exmo, gateio, mexc)
            if (smallest_ask != None and ask_exchange != None):
                percent = get_diff_percent(bid_exchange['price'], biggest_bid['price'])
                if percent > 0.4:
                    await sendMessage(telegram, symbol, biggest_bid['amount'], biggest_bid['price'], 
                                bid_exchange['price'], bid_exchange['name'], percent, buy_on_vvs=False)

    print(result_list)


def get_price_coin(driver, price_list, first_coin, second_coin, ask_prices, bid_prices):

    time.sleep(3)

    control = driver.find_elements(By.ID, "pair")
    check_value = control[0].text

    while check_value != first_coin:
        try:
            buttons = driver.find_elements(By.CLASS_NAME, 'open-currency-select-button')
            buttons[0].click()
            delay()
        except:
            try:
                close_button = driver.find_elements(By.CLASS_NAME, 'inQzxP')
                close_button[0].click()
                delay()
            except:
                pass
        try:
            crypto = driver.find_element(By.ID, 'token-search-input')
            crypto.send_keys(first_coin)
            delay()
            crypto.send_keys(Keys.ENTER)
            delay()
            control = driver.find_elements(By.ID, "pair")
            check_value = control[0].text
        except:
            control = driver.find_elements(By.ID, "pair")
            check_value = control[0].text
            pass

    control = driver.find_elements(By.ID, "pair")
    check_value = control[1].text

    while check_value != second_coin:
        try:
            buttons = driver.find_elements(By.CLASS_NAME, 'open-currency-select-button')
            buttons[1].click()
            delay()
        except:
            try:
                close_button = driver.find_elements(By.CLASS_NAME, 'inQzxP')
                close_button[0].click()
                delay()
            except:
                pass
        try:
            crypto = driver.find_element(By.ID, 'token-search-input')
            crypto.send_keys(second_coin)
            delay()
            crypto.send_keys(Keys.ENTER)
            delay()
            control = driver.find_elements(By.ID, "pair")
            check_value = control[1].text
        except:
            control = driver.find_elements(By.ID, "pair")
            check_value = control[1].text
            pass

    entry = driver.find_elements(By.CLASS_NAME, 'token-amount-input')

    for price_to_check in price_list:
        entry[0].clear()
        try:
            entry[1].clear()
        except:
            delay()
        delay()
        entry[0].send_keys(price_to_check)
        delay()

        control = driver.find_elements(
            By.XPATH, "//input[@title='Token Amount']")
        check_value = control[0].get_attribute(
            'value')  # recupero attributo 'value'

        if check_value != price_to_check:

            while check_value != price_to_check:
                try:
                    entry[1].clear()
                    entry[0].clear()
                    delay()
                    control[0].clear()
                    control[1].clear()
                    entry[0].send_keys(price_to_check)
                    delay()
                    check_value = control[0].get_attribute('value')
                    delay()
                    if check_value == price_to_check:
                        continue
                except:
                    control[0].clear()
                    entry[0].clear()
                    try:
                        entry[1].clear()
                        control[1].clear()
                        delay()
                    except:
                        delay()
                    entry[0].send_keys(price_to_check)
                    delay()
                    check_value = control[0].get_attribute('value')
                    delay()
                    if check_value == price_to_check:
                        continue

        price_element = driver.find_elements(By.CLASS_NAME, 'eOccyd')
        try:
            price_label = price_element[0].text
        except:
            continue
        price = price_label.split('\n')
        price = price[1].split(' ')
        ask_prices[price_to_check] = float(price[0])
        delay()
        change_to_sell = driver.find_elements(By.CLASS_NAME, '_1cvvxtw1')
        try:
            change_to_sell[0].click()
        except:
            continue
        delay()
        price_element = driver.find_elements(By.CLASS_NAME, 'eOccyd')
        try:
            price_label = price_element[0].text
            price = price_label.split('\n')
            price = price[1].split(' ')
        except:
            change_to_sell = driver.find_elements(By.CLASS_NAME, '_1cvvxtw1')
            change_to_sell[0].click()
            continue
        change_in_stable = driver.find_elements(By.CLASS_NAME, '_1nzuaz740l')
        try:
            change_in_stable[0].click()
        except:
            continue
        delay()
        price_element = driver.find_elements(By.CLASS_NAME, 'eOccyd')
        try:
            price_label = price_element[0].text
            price = price_label.split('\n')
            price = price[1].split(' ')
        except:
            continue
        price = price_label.split(' ')
        bid_prices[price_to_check] = float(price[0])

        change_to_sell[0].click()
        change_in_stable[0].click()
        delay()
        try:
            entry[1].clear()
            entry[0].clear()
        except:
            entry[0].clear()
        delay()

    response = dict()
    response['ask'] = ask_prices
    response['bid'] = bid_prices
    return response


def delay():
    time.sleep(0.5)