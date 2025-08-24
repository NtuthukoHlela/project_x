# var_index = ((cleaned_data.columns).tolist()).index(volume) + 1
# cleaned_data.insert(var_index, price_change, price_change_pct)


'''
#within column function
def ml_variables_within_column():
    data = pd.read_excel("raw_full_data.xlsx")
    for i in data.columns:
        if i != "Date":
            data["avg_" + str(i)] = (data[str(i)]).rolling(window=10).mean()

    data.to_excel("processed_cleaned_data.xlsx")
    return  data



ml_variables_within_column()

'''
import yfinance as yf
c = yf.Ticker("TSLA").earnings
print(c)