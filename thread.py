# -*- coding: utf-8 -*-
"""
Created on Wed May 27 03:01:05 2020

@author: laksh
"""

# Import libraries
import threading, time
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from requests.exceptions import ConnectionError

# tsx = pd.read_csv("tsx_raw.csv")
# tsxv = pd.read_csv("tsxv_raw.csv")
# nasdaq = pd.read_csv("nasdaq_raw.csv")
nyse = pd.read_csv("nyse_raw.csv")

def scraper(data, saveas, us):   
    driver = webdriver.Chrome(executable_path=r"C:\Users\laksh\Desktop\Scrapers\Kijiji-bot\chromedriver.exe")
    
    counter = len(data)
    for i in range(len(data)):
        try:
            ticker = data.Symbol[i]
            driver.get(f'https://web.tmxmoney.com/company.php?qm_symbol={ticker}{us}')
            data.Company[i] = driver.find_element_by_xpath('//*[@id="contentWrapper"]/div/div/div/div[1]/div/div[2]/div[1]/div[1]/h4').text
            data.Sector[i] = driver.find_element_by_xpath('//*[@id="pane-news"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div[2]').text
            data.Industry[i] = driver.find_element_by_xpath('//*[@id="pane-news"]/div/div/div[1]/div/div[2]/div[2]/div/div[3]/div[2]').text
            data.NAICS[i] = driver.find_element_by_xpath('//*[@id="pane-news"]/div/div/div[1]/div/div[2]/div[2]/div/div[5]/div[2]').text
            data.Price[i] = driver.find_element_by_xpath('//*[@id="contentWrapper"]/div[1]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div/span/span').text
            counter = counter - 1
            print (f'{counter} tickers remaining')
        except IndexError:
            data.Company[i] = 'nan'
            data.Sector[i] = 'nan'
            data.Industry[i] = 'nan'
            data.NAICS[i] = 'nan'
            data.Price[i] = 'nan' 
        except ConnectionError:
            data.Company[i] = 'nan'
            data.Sector[i] = 'nan'
            data.Industry[i] = 'nan'
            data.NAICS[i] = 'nan'
            data.Price[i] = 'nan'
        except TypeError:
            data.Company[i] = 'nan'
            data.Sector[i] = 'nan'
            data.Industry[i] = 'nan'
            data.NAICS[i] = 'nan'
            data.Price[i] = 'nan'
        except NoSuchElementException:
            data.Company[i] = 'nan'
            data.Sector[i] = 'nan'
            data.Industry[i] = 'nan'
            data.NAICS[i] = 'nan'
            data.Price[i] = 'nan'
    
    driver.close()
    data.to_csv(saveas, index=False)

# threadTsx = threading.Thread(target=scraper,args=(tsx, 'tsx_parsed.csv', ''))
# threadTsxv = threading.Thread(target=scraper,args=(tsxv,'tsxv_parsed.csv', ''))
# threadNasdaq = threading.Thread(target=scraper,args=(nasdaq,'nasdaq_parsed.csv', ':us'))
threadNyse = threading.Thread(target=scraper,args=(nyse,'nyse_parsed.csv', ':us'))

# threadTsx.start()
# threadTsxv.start()
# threadNasdaq.start()
threadNyse.start()
