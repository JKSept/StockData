import numpy as py
import pandas as pd
import requests
import math
from scipy import stats
import xlsxwriter

#Import raw stock data from API call file
from api_call import stock_data

#Intialize a dataframe to store useful information from raw stock data
df_columns = ['Ticker', 'Price', 'Market Cap', 'Change Percent']
df = pd.DataFrame(columns=df_columns)

#Loop through each symbol in stock data dictionary and add relevant infomation to dataframe
for symbol in stock_data:

    price = stock_data[symbol]['quote']['latestPrice']
    mcap = stock_data[symbol]['quote']['marketCap']
    change = stock_data[symbol]['quote']['changePercent']
    df.loc[len(df)] = [symbol, price, mcap, change]







