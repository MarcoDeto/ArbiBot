from webdriver_manager.chrome import ChromeDriverManager # pip install webdriver-manager
from selenium.webdriver import Safari, Edge, Chrome # pip install selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import tkinter as tk

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from services.utilities import clickInterval





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
        price_usdc = {}
        get_vvs_price_USDC(driver, importo, price_usdc)
        get_vvs_prezzo_VVS(driver)
        
#quanto ti costa comprarlo
# a quanto lo rivendi
def get_vvs_price_USDC(driver, importo, price_usdc):
    
        buttons = driver.find_elements(By.CLASS_NAME, 'open-currency-select-button')
        buttons[0].click()
        delay()
        
        crypto = driver.find_element(By.ID, 'token-search-input')
        crypto.send_keys('USDC')
        delay()
        crypto.send_keys(Keys.ENTER)
        delay()
        
        #importo = driver.find_element(By.CLASS_NAME, 'token-amount-input')
        #importo.send_keys('2000')
        #delay()
        
        buttons = driver.find_elements(By.CLASS_NAME, 'open-currency-select-button')
        buttons[1].click()
        delay()
        
        crypto = driver.find_element(By.ID, 'token-search-input')
        crypto.send_keys('VVS')
        delay()
        crypto.send_keys(Keys.ENTER)
        delay()
        
        entry = driver.find_element(By.CLASS_NAME, 'token-amount-input')
        
        for prezzo in importo :
            
            entry.clear()
            entry.send_keys(prezzo)
            delay()
            
            busdc = driver.find_elements(By.CLASS_NAME, 'liRUbv')
        
            bprezzo = busdc[3].text
            price = bprezzo.split(' ')
            #return float(price[0])
            print(float(price[0]))
            price_usdc[prezzo] = float(price[0])
            print(price_usdc)
    
def get_vvs_prezzo_VVS(driver):
        delay()

        buttons = driver.find_elements(By.CLASS_NAME, 'open-currency-select-button')
        buttons[0].click()
        delay()
        
        crypto = driver.find_element(By.ID, 'token-search-input')
        crypto.send_keys('VVS')
        delay()
        crypto.send_keys(Keys.ENTER)
        delay()
    
        buttons = driver.find_elements(By.CLASS_NAME, 'open-currency-select-button')
        buttons[1].click()
        delay()
        
        crypto = driver.find_element(By.ID, 'token-search-input')
        crypto.send_keys('USDC')
        delay()
        crypto.send_keys(Keys.ENTER)
        delay()
        
        importo = driver.find_elements(By.CLASS_NAME, 'token-amount-input')
        importo[1].clear()
        importo[1].send_keys('2000')
        delay()
        
        bvvs = driver.find_elements(By.CLASS_NAME, 'liRUbv')
        testo1 = bvvs[3].text
        #print(testo1)
        testo2 = testo1.split(' ')
        #print(testo2[1])
        
        if testo2[1] == 'USDC' :
            inverti = driver.find_elements(By.CLASS_NAME, 'iziQoG')
            inverti[0].click()
        
            prezzo = bvvs[3].text
            price = prezzo.split(' ')
            return float(price[0])
            #print(float(price[0]))
            
        else :
            
            prezzo = bvvs[3].text
            price = prezzo.split(' ')
            return float(price[0])
            #print(float(price[0]))
            
       
    #except:
        '''
        time.sleep(2)
        screenshotbutton = safariDriver.find_element_by_class_name('getimage')
        screenshotbutton.click()
        time.sleep(3)
        imageLink = safariDriver.find_element_by_class_name('textInput-3WRWEmm7-')
        return(imageLink.get_attribute('value'), safariDriver.current_url)
        '''
    #cambiare coi selezionata selezionare coin del sito
    #selezionare coin da cambiare con usdc
    #inserire soprea usdc e inserire soldi per verificare lo scambio click tasto inversione
    #leggere valore e salvare su una variabile

def delay():
    time.sleep(1)
    

get_vvs_finance()

