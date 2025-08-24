'''
programmer: ntuthuko hlela
goal: process the stock data / add new custom indicators
date: 17.08.2025
'''

import pandas as pd
import numpy as np
import re



cleaned_data = pd.read_excel("raw_data_cleaned.xlsx", index_col=0, header=0)

#function that handles between-columns calculations
def columns_var_calcs(col_1, col_2, metric_name, ticker_name):
    x1 = ticker_name + "_" +  col_1
    x2 = ticker_name + "_" +  col_2
    cleaned_data[ticker_name + "_" + metric_name] = np.round(np.array((cleaned_data[x2] - cleaned_data[x1]) / (cleaned_data[x1])) * 100, 2)


def ml_variables_descriptive():
    for i in cleaned_data.columns:

        var_filter = re.findall("(Open*)", i)   #creating this so that I can only loop 1 time per ticker
        var_filter_1 = "".join(var_filter)


        if i != "Date" and var_filter_1 !="":
            end_of_ticker_name = re.search("_", i)
            ticker_name = i[:end_of_ticker_name.start()]


            #possible y-vars
            columns_var_calcs("Open", "Close", "price_change_pct", ticker_name)
            columns_var_calcs("Low", "High", "low_to_high_pct", ticker_name)
            columns_var_calcs("Open", "High", "open_to_high_pct", ticker_name)
            columns_var_calcs("High", "Close", "high_to_close_pct", ticker_name)
            columns_var_calcs("Open", "Low", "open_to_low_pct", ticker_name)
            columns_var_calcs("Low", "Close", "low_to_close_pct", ticker_name)


    #sorting the data by date
    cleaned_data["Date"] = pd.to_datetime(cleaned_data["Date"])
    cleaned_data.sort_values("Date", inplace=True, ascending=False)
    cleaned_data.to_excel("raw_full_data.xlsx", index=False)

    return cleaned_data

ml_variables_descriptive()
def final_data_cleaning():
    '''1) making y-today correspond with x-yesterday. 2) sorting the colums such that ticker vars are grouped together. 3) preparing the variables to be ingested in ML'''
    data = pd.read_excel("raw_full_data.xlsx")



    #ordering the columns alphabetically by ticker
    vars = []
    tickers = []
    for i in data.columns:
        if i != "Date":
            j = (re.search("(_)", i)).start()
            tickers.append(i[:j])
            vars.append(i[j+1:])

    unique_tickers = list(set(tickers))
    unique_vars = list(set(vars))
    unique_tickers.sort()
    unique_vars.sort()

    new_data_frame = pd.DataFrame()
    new_data_frame["Date"] = pd.to_datetime(data["Date"], yearfirst=True)
    for i in unique_tickers:
        for j in unique_vars:
            new_data_frame[i+ "_" +j] = data[i+ "_" + j]
    new_data_frame.to_excel("processed_full_data_1.xlsx", index=False)


final_data_cleaning()
#create a function that reorders the columns and rows (y = today, x == yesterday)


