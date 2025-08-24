'''
programmer: ntuthuko hlela
date: 14.08.2025
goal: scrape data for project x
'''

import yfinance as yf
from ticker_list import ticker_list
print(ticker_list)

ticker_list = ticker_list
raw_pull_data = yf.download(ticker_list, start='2021-01-01', end='2025-06-01', interval='1d', group_by='ticker')
raw_pull_data.to_excel('raw_pull_data.xlsx')
