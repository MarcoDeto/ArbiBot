# pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Safari, Edge, Chrome  # pip install selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import tkinter as tk

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from services.utilities import clickInterval

list_coin = ['USDC/VVS', ] 


def get_vvs_finance():

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

        importo = [2000, 5000, 10000, 15000, 20000]
        first_coin = ''
        second_coin = ''
        price_coin = {}
        result = []
        for coin in list_coin:
            first_coin = coin.split('/')[0]
            second_coin = coin.split('/')[1]
            response = get_first_price_coin(driver, importo, first_coin, second_coin, price_coin)
            result.append(response)
        



#VVS
def get_vvs_price_USDC(driver, importo, first_coin, second_coin, price_coin):
    
    first_coin = 'USDC'
    second_coin = 'VVS'
    
    get_first_price_coin(driver, importo, first_coin, second_coin, price_coin)
    
    return price_coin

def get_usdc_price_vvs(driver, importo, first_coin, second_coin, price_coin):
    
    first_coin = 'VVS'
    second_coin = 'USDC'
    
    get_second_values_coin(driver, importo, first_coin, second_coin, price_coin)
    
    return price_coin

#CRO
def get_cro_price_vvs(driver, importo, first_coin, second_coin, price_coin):
    
    first_coin = 'CRO'
    second_coin = 'VVS'
    
    get_first_price_coin(driver, importo, first_coin, second_coin, price_coin)
    
    return price_coin

def get_vvs_price_cro(driver, importo, first_coin, second_coin, price_coin):
    
    first_coin = 'VVS'
    second_coin = 'CRO'
    
    get_second_values_coin(driver, importo, first_coin, second_coin, price_coin)
    
    return price_coin
    
#EFI
def get_efi_price_vvs(driver, importo, first_coin, second_coin, price_coin):
    
    first_coin = 'EFI'
    second_coin = 'VVS'
    
    get_first_price_coin(driver, importo, first_coin, second_coin, price_coin)
    
    return price_coin

def get_vvs_price_efi(driver, importo, first_coin, second_coin, price_coin):
    
    first_coin = 'VVS'
    second_coin = 'CRO'
    
    get_second_values_coin(driver, importo, first_coin, second_coin, price_coin)
    
    return price_coin
    
#def get_vvs_price_USDC(driver, importo):
def get_first_price_coin(driver, importo, first_coin, second_coin, price_coin):
    
    #price_usdc = {}

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

    entry = driver.find_element(By.CLASS_NAME, 'token-amount-input')
    for prezzo in importo:

        entry.clear()
        entry.send_keys(prezzo)
        delay()

        busdc = driver.find_elements(By.CLASS_NAME, 'liRUbv')
        bprezzo = busdc[3].text
        price = bprezzo.split(' ')
        price_coin[prezzo] = float(price[0])

    #return price_usdc


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
