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
        

        importo = ['500','1000','1500','2000','3000','4000','5000','10000','15000','20000']
        first_coin = ''
        second_coin = ''
        price_coin = {}
        result = []
        for coin in list_coin:
            first_coin = coin_basec
            second_coin = coin
            response = get_first_price_coin(driver, importo, first_coin, second_coin, price_coin)
            result.append(response)
            print(result)
        

    
#def get_vvs_price_USDC(driver, importo):
def get_first_price_coin(driver, importo, first_coin, second_coin, price_coin):
    

    buttons = driver.find_elements(By.CLASS_NAME, 'open-currency-select-button')
    buttons[0].click()
    time.sleep(3)
    
    #coin_list = driver.find_elements(By.CLASS_NAME, list_class_name)
    #print(coin_list[0].text)

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
    
    for prezzo in importo:

        #control = driver.find_elements(By.XPATH, "//input[@title='Token Amount']")
        #valore = control[0].get_attribute('value') #recupero attributo 'value'
        #print(valore)
        #control[0].clear()
        entry[1].clear()
        entry[0].clear()
        delay()  
        entry[0].send_keys(prezzo)
        delay()   
        #sc-fkubCs dCaJGX token-amount-input
        #controla = driver.find_elements(By.CLASS_NAME, 'fPMzfz')
        #print(controla[0].get_attribute('value'))
        #controlb = driver.find_elements(By.CLASS_NAME, 'sc-fkubCs')
        control = driver.find_elements(By.XPATH, "//input[@title='Token Amount']")
        valore = control[0].get_attribute('value') #recupero attributo 'value'
        #if valore != prezzo :
         #   print(valore)
          #  control[0].clear()
           # delay()
        #while  valore :
        
        
        
         #   print(valore)
          #  control[0].clear()
           # delay()
        #while  valore :
        print('valore = ', valore)
        print('prezzo = ', prezzo)
        if valore != prezzo :
            
            while valore != prezzo :
                entry[1].clear()
                entry[0].clear()
                delay()  
                control[0].clear()
                control[1].clear()
                print(prezzo)
                print(valore)
                entry[0].send_keys(prezzo)
                delay()
                valore = control[0].get_attribute('value')
                delay()
                print('valore azz', valore)
                if valore == prezzo:
                    break
    
        #sc-eCjjWe fPMzfz

        #print(control[0].tag_name)
        #print(entry[0].title)
        #entry[0].cancel()
        #entry[0].send_keys(Keys.DELETE)
         
        #entry[0].clear()
        #delay()
        
        #entry[0].send_keys(prezzo)
        #delay()
        

        busdc = driver.find_elements(By.CLASS_NAME, 'liRUbv')
        try :
            bprezzo = busdc[3].text
        except :
            break
        
        price = bprezzo.split(' ')
        price_coin[prezzo] = float(price[0])
        entry[1].clear()
        entry[0].clear()
        delay()
                

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
