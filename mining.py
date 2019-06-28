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
data = pd.read_csv("tsxv.csv")

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
        ticker_naics= soup.findAll('td')[31]
        ticker_price = soup.findAll('span')[0]
        data.Sector[i] = ticker_sector.text
        data.Industry[i] = ticker_industry.text
        data.NAICS[i] = ticker_naics.text
        data.Price[i] = ticker_price.text
        print("Done ticker: " + ticker)
        print(i)
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

for i in range(len(data)):
    try:
        ticker = data.Symbol[i]
        # Set the URL you want to webscrape from
        url = 'https://web.tmxmoney.com/quote.php?qm_symbol='
        url = url + ticker
        # Connect to the URL
        response = requests.get(url)
        
        # Parse HTML and save to BeautifulSoup object¶
        soup = BeautifulSoup(response.text, "html.parser")
        ticker_beta = soup.findAll('td')[9]
        data.Beta[i] = ticker_beta.text
        
        ticker_pe = soup.findAll('td')[31]
        data.PE[i] = ticker_pe.text
        
        ticker_eps = soup.findAll('td')[35]
        data.EPS[i] = ticker_eps.text
        
        print("Done ticker: " + ticker)
        print(i)
    except IndexError:
        data.Beta[i] = 'nan'
        data.PE[i] = 'nan'
        data.EPS[i] = 'nan'
    except ConnectionError:
        data.Beta[i] = 'nan'
        data.PE[i] = 'nan'
        data.EPS[i] = 'nan'
    except TypeError:
        data.Beta[i] = 'nan'
        data.PE[i] = 'nan'
        data.EPS[i] = 'nan'
        
data.to_csv('tsxv_parsed.csv', index=False)