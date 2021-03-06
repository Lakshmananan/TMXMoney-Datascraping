# -*- coding: utf-8 -*-
"""
Created on Wed May 27 03:01:05 2020

@author: laksh
"""

# Import libraries
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from requests.exceptions import ConnectionError

tsx = pd.read_csv("tsx_raw.csv")
tsxv = pd.read_csv("tsxv_raw.csv")
nasdaq = pd.read_csv("nasdaq_raw.csv")

def scraper(data, saveas, us):   
    driver = webdriver.Chrome(executable_path=r"C:\Users\laksh\Desktop\Scrapers\Kijiji-bot\chromedriver.exe")
    
    counter = len(data)
    for i in range(len(data)):
        try:
            ticker = data.Symbol[i]
            driver.get(f'https://web.tmxmoney.com/company.php?qm_symbol={ticker}{us}')
            data.Sector[i] = driver.find_element_by_xpath('//*[@id="pane-news"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div[2]').text
            data.Industry[i] = driver.find_element_by_xpath('//*[@id="pane-news"]/div/div/div[1]/div/div[2]/div[2]/div/div[3]/div[2]').text
            data.NAICS[i] = driver.find_element_by_xpath('//*[@id="pane-news"]/div/div/div[1]/div/div[2]/div[2]/div/div[5]/div[2]').text
            data.Price[i] = driver.find_element_by_xpath('//*[@id="contentWrapper"]/div[1]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div/span/span').text
            counter = counter - 1
            print (f'{counter} tickers remaining')
        except IndexError:
            data.Sector[i] = 'nan'
            data.Industry[i] = 'nan'
            data.NAICS[i] = 'nan'
            data.Price[i] = 'nan' 
        except ConnectionError:
            data.Sector[i] = 'nan'
            data.Industry[i] = 'nan'
            data.NAICS[i] = 'nan'
            data.Price[i] = 'nan'
        except TypeError:
            data.Sector[i] = 'nan'
            data.Industry[i] = 'nan'
            data.NAICS[i] = 'nan'
            data.Price[i] = 'nan'
        except NoSuchElementException:
            data.Sector[i] = 'nan'
            data.Industry[i] = 'nan'
            data.NAICS[i] = 'nan'
            data.Price[i] = 'nan'
    
    driver.close()
    data.to_csv(saveas, index=False)

# scraper(tsx, 'tsx_parsed.csv', '')
# scraper(tsxv,'tsxv_parsed.csv', '')
scraper(nasdaq,'nasdaq_parsed.csv', ':us')