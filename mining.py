# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 14:27:31 2019

@author: laksh
"""

# Import libraries
import pandas as pd
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError

#Load csv file with tickers
data = pd.read_csv("tsx_jun21.csv")

for i in range(len(data)):
    try: 
        ticker = data.Symbol[i]
        # Set the URL you want to webscrape from
        url = 'https://web.tmxmoney.com/company.php?qm_symbol='
        url = url + ticker
        # Connect to the URL
        response = requests.get(url)
            
        # Parse HTML and save to BeautifulSoup object¶
        soup = BeautifulSoup(response.text, "html.parser")
        ticker_sector = soup.findAll('td')[21]
        ticker_industry = soup.findAll('td')[26]
        data.Sector[i] = ticker_sector.text
        data.Industry[i] = ticker_industry.text
        print("Done ticker: " + ticker)
        print(i)
    except IndexError:
        data.Sector[i] = 'nan'
        data.Industry[i] = 'nan'
    except ConnectionError:
        data.Sector[i] = 'nan'
        data.Industry[i] = 'nan'
    except TypeError:
        data.Sector[i] = 'nan'
        data.Industry[i] = 'nan'
        

data.to_csv('jun21_parsed.csv')