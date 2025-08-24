'''
programmer: ntuthuko hlela
goal: test snippets of code
'''
import re
import yfinance as yf
import pandas as pd

'''
l = list(range(1,10))
print(l)
del l[1]
print(l)

p = ['Unnamed: 117',  'Unnamed: 118',  'Unnamed: 119', 'Unnamed: 120', 'CHPT']

final_list = []
for i in p:
    o = re.sub(r'(Unnamed: \d*)', "",i)
    if o != "":
        final_list.append(o)


print(final_list)


s = ["n", "t", "u"]

k = pd.DataFrame({"x": [1,2,3,4], "y": [5,6,7,8]})
x = k["x"].rolling(window=2).sum()
print(type(x))
k["new"] = x
print(k)


j = yf.Ticker("BTC-USD")
print(j.info)

df = pd.DataFrame([1, 2, 3, 4])
h = df[df[0]>1]
print(h)
print(pd.to_datetime("2025-01-01"))
'''
import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
import numpy as np
plt.plot(np.array([1,2,3,4]), np.array([4,5,6,3]))
plt.show()
