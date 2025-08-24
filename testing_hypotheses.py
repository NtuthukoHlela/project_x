import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt


data = pd.read_excel("processed_full_data_1.xlsx")
x = data.columns.str.contains("price_change_pct|Date")

u = data.columns[x]
new_data = data[u]

new_data = new_data[new_data["Date"] > pd.to_datetime("2025-01-01")]
print(len(new_data))

descriptive_stats = []
for i in new_data.columns:

    if i != "Date":
        abv_10_temp = new_data[new_data[i] >= 10]
        abv_10_dates = abv_10_temp["Date"]

        ticker_name = str(i)
        mean = new_data[i].mean()
        median = new_data[i].median()
        std = new_data[i].std()
        abv_10 = len(new_data[new_data[i] >= 10])
        abv_10_price_change = abv_10_temp[i]
        number_of_total_days = len(new_data[i])
        abv_10_to_total_days = round((abv_10 / number_of_total_days), 2)
        abv_5 = len(new_data[new_data[i] >= 5])
        abv_5_to_total_days = round((abv_5 / number_of_total_days), 2)

        descriptive_stats.append({"ticker": ticker_name, "mean": mean, "median": median,
                                  "std": std, "total_days": number_of_total_days, "abv_10": abv_10,
                                  "abv_10_to_total_days": abv_10_to_total_days, "abv_5":
                                      abv_5, "abv_5_to_total_days": abv_5_to_total_days})

g = (pd.DataFrame(descriptive_stats)).sort_values(by=["abv_5", "abv_10"], ascending=False)
g.to_excel("Stats.xlsx", index=False)

