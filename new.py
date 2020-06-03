# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 14:11:37 2020

@author: laksh
"""
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from requests.exceptions import ConnectionError
from multiprocessing import Pool, cpu_count

data = pd.read_csv("tsx_raw.csv")

def selenium_func(data):
    driver = webdriver.Chrome(executable_path=r"C:\Users\laksh\Desktop\Scrapers\Kijiji-bot\chromedriver.exe")
    counter = len(data)
    for i in range(len(data)):
        try:
            ticker = data.Symbol[i]
            driver.get(f'https://web.tmxmoney.com/company.php?qm_symbol={ticker}')
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
            
def run_parallel_selenium_processes(data, selenium_func):

    pool = Pool()

    # max number of parallel process
    ITERATION_COUNT = cpu_count()-1

    count_per_iteration = len(data) / float(ITERATION_COUNT)

    for i in range(0, ITERATION_COUNT):
        list_start = int(count_per_iteration * i)
        list_end = int(count_per_iteration * (i+1))
        pool.apply_async(selenium_func, [data[list_start:list_end]])

run_parallel_selenium_processes(data, selenium_func(data))