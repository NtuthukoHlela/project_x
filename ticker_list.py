'''
programmer: ntuthuko hlela
date: 14.08.2025
goal: ticker_list for project_x
'''

'''
ticker_list = ['TMC', 'PLTR', 'WULF', 'TNXP', 'RIOT', 'RUN', 'SNOW', 'NEGG', 'CHPT', 'CRWV',
               'OPEN', 'NVDA', 'GOOGL', 'AMZN', "BBAI", "GFAI","SOUN","AI","CXAI","INOD","MARK",
    "IONQ","GCT","SMCI","AMD","ARM", "MDB", 'TSLA', 'GM', 'F',]
    '''
ticker_list = ["IONQ","GCT","SMCI","AMD","ARM", "MDB", 'TSLA', 'GM', 'F']

#making sure that we only have unique tickers so that the yfinance api does not panic
print(len(ticker_list))
duplicates = 0
for i in ticker_list:
    if ticker_list.count(i) != 1:
        duplicates +=1
        print(i)

#exit()
if duplicates == 0:
    print("No duplicates found, you can  call the api.")

else:
    print("I found some duplicate tickers, please check the output window.")
    exit()
