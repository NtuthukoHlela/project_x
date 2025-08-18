'''
programmer: ntuthuko hlela
date: 14.08.2025
goal: analyse stock data
'''
import numpy as np
import pandas as pd
from ticker_list import ticker_list
import json
import re

#globals to change
#create_new_raw_data_file = 0

def processing_data():
    '''creating a new excel file to avoid overwriting the existing api call data'''
    create_new_raw_data_file = (input("****>>>  press 1 to run the function or 0 to skip: "))    #only turn on to 1 if you have changed something in the scraping_data.py
    if (create_new_raw_data_file) == str(1):
        print("running the function!!")
        raw_data = pd.read_excel('raw_pull_data.xlsx', header=0)
        columns = {"raw_columm_names": raw_data.columns.tolist()}
        open("raw_columns.json", "w").write(json.dumps(columns))
        raw_data.to_excel("raw_data_1.xlsx")
    else:
        print("skipping the function!!")
processing_data()


def cleaning_col_names():
    '''getting the actual column names in my dataframe'''

    final_list_of_col_names = []
    col_names_list = ((pd.read_json("raw_columns.json"))["raw_columm_names"]).tolist()
    for i in col_names_list:
        col_name = re.sub(r'(Unnamed: \d*)', "", i)
        if col_name != "" and col_name!= "Ticker":
            final_list_of_col_names.append(col_name)
    return final_list_of_col_names


def preliminary_cleaning():
    raw_data_df = pd.read_excel("raw_data_1.xlsx", header=1, index_col=0)
    date = np.array(raw_data_df["Price"])
    raw_data_df.insert(0, "Date",date, allow_duplicates=False)
    del raw_data_df["Price"]
    raw_data_df.drop([1], axis=0, inplace=True)
    raw_data_df.dropna(axis=1, inplace=True)

     #renaming the first ticker using the index so that I can pull the actual name from a list of ticker names
    raw_data_df.rename({"Open": "Open.0",
                                "High": "High.0",
                                "Low": "Low.0", "Close": "Close.0",
                                "Volume": "Volume.0"},
                                axis=1, inplace=True)

    for i in raw_data_df.columns:
        if i != "Date":
            var_name = re.findall("(\D)", i)
            var_name_cleaned = ("".join(var_name)).replace(".", "_")

            index_raw = re.findall("(\d*)", i)
            col_index_array = np.array(index_raw)
            index_cleaned = int((col_index_array[col_index_array!=""])[0])

            all_tickers = cleaning_col_names()

            final_var_name = var_name_cleaned + str(all_tickers[index_cleaned])
            raw_data_df.rename({str(i): str(final_var_name)}, axis=1, inplace=True)

    raw_data_df.to_excel("raw_data_cleaned.xlsx")
    return raw_data_df

preliminary_cleaning()

