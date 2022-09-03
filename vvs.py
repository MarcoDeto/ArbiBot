# pip install webdriver-manager
from lib2to3.pgen2 import driver
from turtle import clear
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Safari, Edge, Chrome  # pip install selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import tkinter as tk

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from services.utilities import clickInterval

coin_basec = 'USDC'
coin_baset = 'USDT'

list_coin = ['CRO', '1INCH', 'AAVE', 'ACA', 'ACH', 'ADA', 'AGLD', 'AKT', 'ALGO', 'ALI', 
             'ALICE', 'ANKR', 'APE', 'AR', 'ARGO', 'ATOM', 'AURORA', 'AVAX', 'AXS','BAT', 
             'BCH', 'bCRO', 'BIFI', 'BOSON', 'CELR', 'CHR', 'CHZ', 'CKB', 'COMP', 'CROGE', 
             'CRV', 'CSPR', 'DAI', 'DAR', 'DARK', 'DERC', 'DOGE', 'DOT', 'DUSD', 'DYDX', 
             'EFI', 'EGLD', 'ELON', 'ENJ', 'ENS', 'EOS', 'EPX', 'ETC', 'ETH', 'FER',
             'FIL', 'FITFI', 'FLOW', 'FTM', 'GAL', 'GALA', 'GLMR', 'GRT', 'HBAR', 'HNT',
             'HOD', 'HOT', 'ICP', 'ICX', 'IMX', 'INJ', 'JASMY', 'KNC', 'KRL', 'KSM', 'LDO', 
             'LINK', 'LRC', 'LTC', 'MANA', 'MATIC', 'MC', 'MKR', 'MTD', 'NEAR', 'NEO', 'NESS', 
             'OGN', 'OMG', 'ONE', 'OPL', 'PAXG', 'PENDLE', 'PLA', 'QNT', 'QRDO', 'QTUM', 
             'RADAR', 'RARE', 'REN', 'REP', 'RNDR', 'RUNE', 'SAND', 'SHIB', 'SINGLE', 'SKY', 
             'SLP', 'SNT', 'SNX', 'SOL', 'SPELL', 'SPS', 'SRM', 'STX', 'SUSHI', 'THETA', 'TONIC', 
             'TUSD', 'UMA', 'UNI', 'V3CRO', 'V3DUSD', 'V3S', 'V3TONIC', 'VERSA', 'VET', 'VOXEL', 
             'VSHARE', 'VTHO', 'WBTC', 'WCRO', 'WEMIX', 'WOO', 'XLM', 'XNO', 'XTZ', 'XYO', 'YFI', 
             'YGG', 'ZILL']

list_coina = ['ACH', '1INCH']

#list_class_name = 'sc-gsTEea'#'crQsOR'  

def get_vvs_finance():

    result_list = []

    try:
        driver = Safari()
        driver.maximize_window()
    except:
        # try:
        #     opera_driver_manager = OperaDriverManager().install()
        #     driver = Opera(service=Service(opera_driver_manager))
        # except:
        try:
            chrome_driver_manager = ChromeDriverManager().install()
            driver = Chrome(service=Service(chrome_driver_manager))
        except:
            driver = Edge()
            driver.maximize_window()

    #try:
        time.sleep(1)
        driver.get('https://vvs.finance/swap')
        time.sleep(3)
        
        #buttons = driver.find_elements(By.CLASS_NAME, 'open-currency-select-button')
        #buttons[0].click()
        #time.sleep(3)
        #driver.execute_script("window.stop();")
        

        importo = ['500','750','1000','1250','1500','2000','3000','4000','5000','10000','15000','20000']
        first_coin = ''
        second_coin = ''
        price_coin = {}
        result = []
        for coin in list_coin:
            first_coin = coin_basec
            second_coin = coin
            result = dict()
            result['coin'] = second_coin
            result['value'] = get_first_price_coin(driver, importo, first_coin, second_coin, price_coin)
            result_list.append(result)
        
        print(result_list)
            
        

    
#def get_vvs_price_USDC(driver, importo):
def get_first_price_coin(driver, price_list, first_coin, second_coin, price_coin):
    

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

        print('valore = ', check_value)
        print('prezzo = ', price_to_check)
        if check_value != price_to_check :
            
            while check_value != price_to_check :
                entry[1].clear()
                entry[0].clear()
                delay()  
                control[0].clear()
                control[1].clear()
                print(price_to_check)
                print(check_value)
                entry[0].send_keys(price_to_check)
                delay()
                check_value = control[0].get_attribute('value')
                delay()
                print('valore azz', check_value)
                if check_value == price_to_check:
                    break
                

        busdc = driver.find_elements(By.CLASS_NAME, 'liRUbv')
        try :
            bprezzo = busdc[3].text
        except :
            break
        
        price = bprezzo.split(' ')
        price_coin[price_to_check] = float(price[0])
        entry[1].clear()
        entry[0].clear()
        delay()
                

    return price_coin


#def get_usdc_values_vvs(driver, importo):
def get_second_values_coin(driver, importo, first_coin, second_coin, price_coin):
    
    #price_vvs = {}
    
    delay()

    buttons = driver.find_elements(
        By.CLASS_NAME, 'open-currency-select-button')
    buttons[0].click()
    delay()

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
    delay()

    
    for prezzo in importo:

        entry[1].clear()
        entry[1].send_keys(prezzo)
        delay()

        busdc = driver.find_elements(By.CLASS_NAME, 'liRUbv')
        bprezzo = busdc[3].text
        price = bprezzo.split(' ')
        price_coin[prezzo] = float(price[0])

    #return price_vvs



def delay():
    time.sleep(1)


get_vvs_finance()
