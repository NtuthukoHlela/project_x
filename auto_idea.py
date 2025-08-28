import yfinance as yf


oems_stocks = yf.Industry("auto-manufacturers")
suppliers_stocks = yf.Industry("auto-parts")
x = (suppliers_stocks.top_companies).index
print(x)
#print(suppliers_stocks.top_companies["symbol"])
