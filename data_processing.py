'''
programmer: ntuthuko hlela
goal: process the stock data / add new custom indicators
date: 17.08.2025
'''

import pandas as pd
import numpy as np
import re



cleaned_data = pd.read_excel("raw_data_cleaned.xlsx", index_col=0, header=0)


def ml_variables():
    new_ml_variables = {}
    for i in cleaned_data.columns:
        var_filter = re.findall("(Open_*)", i)   #creating this so that I can only loop 1 time per ticker
        var_filter_1 = "".join(var_filter)

        if i != "Date" and var_filter_1 != "" :
            ticker_name = "".join(re.findall("(_[A-Z]*)", i))

            #price change (close - open)
            close = "Close" + ticker_name
            open = "Open" + ticker_name
            price_change = "price_change_pct" + ticker_name
            price_change_pct = np.array( (cleaned_data[close] - cleaned_data[open]) / (cleaned_data[open]) )*100
            price_change_pct = np.round(price_change_pct, 2)
            new_ml_variables[price_change] = price_change_pct

    x = pd.DataFrame.from_dict(new_ml_variables)
    raw_full_data = pd.concat([cleaned_data, x], axis=1)
    raw_full_data.to_excel("raw_full_data.xlsx")
    print(raw_full_data[["Open_TSLA", "Close_TSLA", "price_change_pct_TSLA"]])

    return new_ml_variables

ml_variables()

#create a function that reorders the columns and rows (y = today, x == yesterday)


