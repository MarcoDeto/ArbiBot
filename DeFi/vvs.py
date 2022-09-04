# pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Safari, Edge, Chrome  # pip install selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from Exchange.cryptocom import *

from config import AMOUNT_LIST
from telegram import sendMessage
from utilities import *


coin_basec = 'USDC'
coin_baset = 'USDT'

coin_list = ['MTD', 'FER', 'CRO', '1INCH', 'AAVE', 'ACA', 'ACH', 'ADA', 'AGLD', 'AKT', 'ALGO', 'ALI', 
             'ALICE', 'ANKR', 'APE', 'AR', 'ARGO', 'ATOM', 'AURORA', 'AVAX', 'AXS','BAT', 
             'BCH', 'bCRO', 'BIFI', 'BOSON', 'CELR', 'CHR', 'CHZ', 'CKB', 'COMP', 'CROGE', 
             'CRV', 'CSPR', 'DAI', 'DAR', 'DARK', 'DERC', 'DOGE', 'DOT', 'DUSD', 'DYDX', 
             'EFI', 'EGLD', 'ELON', 'ENJ', 'ENS', 'EOS', 'EPX', 'ETC', 'ETH', 'FER', 'FIL', 
             'FIRA', 'FITFI', 'FLOW', 'FTM', 'GAL', 'GALA', 'GLMR', 'GRT', 'HBAR', 'HNT',
             'HOD', 'HOT', 'ICP', 'ICX', 'IMX', 'INJ', 'JASMY', 'KNC', 'KRL', 'KSM', 'LDO', 
             'LINK', 'LRC', 'LTC', 'MANA', 'MATIC', 'MC', 'MKR', 'MTD', 'NEAR', 'NEO', 'NESS', 
             'OGN', 'OMG', 'ONE', 'OPL', 'PAXG', 'PENDLE', 'PLA', 'QNT', 'QRDO', 'QTUM', 'RADAR',
             'RARE', 'REN', 'REP', 'RNDR', 'RUNE', 'SAND', 'SHIB', 'SINGLE', 'SKY', 'SLP', 'SNT', 
             'SNX', 'SOL', 'SPELL', 'SPS', 'SRM', 'STX', 'SUSHI', 'THETA', 'TONIC', 'TUSD', 'UMA', 
             'UNI', 'V3CRO', 'V3DUSD', 'V3S', 'V3TONIC', 'VERSA', 'VET', 'VOXEL', 'VSHARE', 'VTHO',
             'WBTC', 'WCRO', 'WEMIX', 'WOO', 'XLM', 'XNO', 'XTZ', 'XYO', 'YFI', 'YGG', 'ZILL']


async def get_vvs_finance(telegram):

    result_list = []

    try:
        chrome_driver_manager = ChromeDriverManager().install()
        driver = Chrome(service=Service(chrome_driver_manager))
    except:
        pass
        # try:
        #     opera_driver_manager = OperaDriverManager().install()
        #     driver = Opera(service=Service(opera_driver_manager))
        # except:
    
    time.sleep(1)
    driver.get('https://vvs.finance/swap')
    time.sleep(3)

    stable_coin = coin_basec
    result = []
    for second_coin in coin_list:
        symbol = get_symbol(second_coin, stable_coin)
        cryptocom = get_ticker_value(symbol)
        if cryptocom == None: continue
        result = dict()
        ask_prices = {}
        bid_prices = {}
        prices = get_price_coin(driver, AMOUNT_LIST, stable_coin, second_coin, ask_prices, bid_prices)
        result['coin'] = second_coin
        result['value'] = prices
        result_list.append(result)
        smallest_ask = get_smallest_ask(prices['ask'])
        biggest_bid = get_biggest_bid(prices['bid'])
        percent = get_diff_percent(smallest_ask['price'], cryptocom['bid'])
        if percent > 0:
            await sendMessage(telegram, symbol, smallest_ask['amount'], smallest_ask['price'], cryptocom['bid'], percent, buy_on_vvs = True)

        percent = get_diff_percent(cryptocom['ask'], biggest_bid['price'])
        if percent > 0:
            await sendMessage(telegram, symbol, biggest_bid['amount'], cryptocom['ask'], biggest_bid['price'], percent, buy_on_vvs = False)
    
    print(result_list)
            
        
def get_price_coin(driver, price_list, first_coin, second_coin, ask_prices, bid_prices):
    
    buttons = driver.find_elements(By.CLASS_NAME, 'open-currency-select-button')
    buttons[0].click()
    time.sleep(3)

    crypto = driver.find_element(By.ID, 'token-search-input')
    crypto.send_keys(first_coin)
    delay()
    crypto.send_keys(Keys.ENTER)
    delay()

    buttons = driver.find_elements(
        By.CLASS_NAME, 'open-currency-select-button')
    buttons[1].click()
    delay()

    crypto = driver.find_element(By.ID, 'token-search-input')
    crypto.send_keys(second_coin)
    delay()
    crypto.send_keys(Keys.ENTER)
    delay()

    entry = driver.find_elements(By.CLASS_NAME, 'token-amount-input')
    
    for price_to_check in price_list:
        entry[1].clear()
        entry[0].clear()
        delay()  
        entry[0].send_keys(price_to_check)
        delay()   

        control = driver.find_elements(By.XPATH, "//input[@title='Token Amount']")
        check_value = control[0].get_attribute('value') #recupero attributo 'value'

        if check_value != price_to_check :
            
            while check_value != price_to_check :
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
                    break
                
        price_element = driver.find_elements(By.CLASS_NAME, 'liRUbv')
        try:
            price_label = price_element[3].text
        except:
            break
        price = price_label.split(' ')
        ask_prices[price_to_check] = float(price[0])
        delay()
        change_to_sell = driver.find_elements(By.CLASS_NAME, 'fbkFTK')
        change_to_sell[0].click()
        delay()
        price_element = driver.find_elements(By.CLASS_NAME, 'liRUbv')
        try:
            price_label = price_element[3].text
        except:
            change_to_sell = driver.find_elements(By.CLASS_NAME, 'fbkFTK')
            change_to_sell[0].click()
            break
        change_in_stable = driver.find_elements(By.CLASS_NAME, 'kxCpqo')
        change_in_stable[0].click()
        delay()
        price_element = driver.find_elements(By.CLASS_NAME, 'liRUbv')
        try:
            price_label = price_element[3].text
        except:
            break
        price = price_label.split(' ')
        bid_prices[price_to_check] = float(price[0])

        change_to_sell[0].click()
        change_in_stable[0].click()
        entry[1].clear()
        entry[0].clear()
        delay()

    response = dict()
    response['ask'] = ask_prices
    response['bid'] = bid_prices
    return response


def delay():
    time.sleep(1)
