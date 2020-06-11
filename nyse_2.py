# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:16:46 2020

@author: laksh
"""

import threading, time
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from requests.exceptions import ConnectionError

tickers = []
driver = webdriver.Chrome(executable_path=r"C:\Users\laksh\Desktop\Scrapers\Kijiji-bot\chromedriver.exe")
driver.get('https://www.nyse.com/listings_directory/stock#')

for i in range(640):
    tickers.append(driver.find_element_by_xpath('//*[@id="content-aa395ece-e341-4621-9695-3642148ea198"]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/a').text)
    tickers.append(driver.find_element_by_xpath('//*[@id="content-aa395ece-e341-4621-9695-3642148ea198"]/div/div[2]/div[1]/table/tbody/tr[2]/td[1]/a').text)
    tickers.append(driver.find_element_by_xpath('//*[@id="content-aa395ece-e341-4621-9695-3642148ea198"]/div/div[2]/div[1]/table/tbody/tr[3]/td[1]/a').text)
    tickers.append(driver.find_element_by_xpath('//*[@id="content-aa395ece-e341-4621-9695-3642148ea198"]/div/div[2]/div[1]/table/tbody/tr[4]/td[1]/a').text)
    tickers.append(driver.find_element_by_xpath('//*[@id="content-aa395ece-e341-4621-9695-3642148ea198"]/div/div[2]/div[1]/table/tbody/tr[5]/td[1]/a').text)
    tickers.append(driver.find_element_by_xpath('//*[@id="content-aa395ece-e341-4621-9695-3642148ea198"]/div/div[2]/div[1]/table/tbody/tr[6]/td[1]/a').text)
    tickers.append(driver.find_element_by_xpath('//*[@id="content-aa395ece-e341-4621-9695-3642148ea198"]/div/div[2]/div[1]/table/tbody/tr[7]/td[1]/a').text)
    tickers.append(driver.find_element_by_xpath('//*[@id="content-aa395ece-e341-4621-9695-3642148ea198"]/div/div[2]/div[1]/table/tbody/tr[8]/td[1]/a').text)
    tickers.append(driver.find_element_by_xpath('//*[@id="content-aa395ece-e341-4621-9695-3642148ea198"]/div/div[2]/div[1]/table/tbody/tr[9]/td[1]/a').text)
    tickers.append(driver.find_element_by_xpath('//*[@id="content-aa395ece-e341-4621-9695-3642148ea198"]/div/div[2]/div[1]/table/tbody/tr[10]/td[1]/a').text)
    driver.find_element_by_xpath('//*[@id="content-aa395ece-e341-4621-9695-3642148ea198"]/div/div[2]/div[2]/div/ul/li[8]/a').click()
    time.sleep(1)
    print(f'Done page {i}')
    
    
