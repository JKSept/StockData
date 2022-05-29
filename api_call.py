import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math


#Reading and saving list of stock symbols for API call and a testing variable
sp_symbols = pd.read_csv('sp_500_stocks.csv')
symbols_list = sp_symbols['Symbol'].tolist()



#Importing private API key from
from secrets import IEX_CLOUD_API as token


#Function to divide symbol list into chunks for bacth API calls
def symbol_chunker(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

#Using the symbol chunker function on the symbol list
symbol_groups = list(symbol_chunker(symbols_list, 100))

#Creating a list containing the chunked symbols lists
symbol_chunks_list = []
for i in range(0, len(symbol_groups)):
    symbol_chunks_list.append(','.join(symbol_groups[i]))


#Creating empty dictionary to fill with stock data from API calls
stock_data = {}

for symbol_list in symbol_chunks_list:
    batch_api_call_url = f'https://cloud.iexapis.com/stable/stock/market/batch?symbols={symbol_list}&types=quote&token={token}'

    data = requests.get(batch_api_call_url).json()

    #Looping back through symbols and trying to add data from that symbols call into stock_data dictionary
    # skipping over any symbols that did not return data and could cause a KeyError
    for symbol in symbol_list.split(','):
        try:
            stock_data[symbol] = data[symbol]
        except KeyError:
            continue




