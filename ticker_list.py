'''
programmer: ntuthuko hlela
date: 14.08.2025
goal: ticker_list for project_x
'''

ticker_list = ['TSLA', 'GOOG', 'AAPL', 'NVDA' ,'INTC', 'OPEN',
               'NU', 'WULF', 'RUN', 'NIO', 'UNH', 'BMNR', 'PLTR',
               'LCID', 'RIVN', 'AMCR', 'AAL','RBLX', 'AMZN', 'CSCO',
               'F', 'AMD', 'MSFT', 'UBER', 'LYFT',  'META', 'MDB', 'NFLX',
               'BHC', 'GTLB', 'UEC', 'UAA', 'SPOT', 'ARWR', 'OS', 'NEGG', 'AMAT',
               'GLOB', 'TNXP', 'KLAC', 'TGLS', 'RIOT', 'SOC', 'SLNO', 'RGTI', 'LRCX',
               'AIT', 'QBTS', 'LION', 'ROAD', 'FORM', 'SEAT', 'ENPH', 'MRNA',
               'CHPT', 'CE', 'SNLKF', 'LYEL', 'CNC', 'NVO', 'DOw', 'PCVX',
               'OGN', 'INSP', 'LINE', 'FRPT', 'MOH', 'REGN', 'IT', 'OLN', 'ONTO', 'TFX',
               'TTD', 'AVTR', 'RXO', 'WFRD', 'COLD', 'BKRR', 'COTY', 'ALIT', 'CIVI', 'ICLR',
               'XRAY', 'WPP', 'LYB', 'RARE', 'LNTH', 'ASGN', 'ANF', 'FUN', 'RIG', 'UNICY', 'SPSC',
               'ELV', 'PTEN', 'ENR', 'TDC', 'VSH', 'CENT', 'ATKR', 'YELP', 'ZGN', 'IOSP', 'LSFT',
               'SRPT', 'DBRG', 'AGIO', 'GOF', 'IVT', 'WEN', 'FOLD', 'BTU', 'CRGY', 'CC',
               'ABR', 'APPN', 'PK', 'PRCT', 'IMVT', 'CENTA', 'JJSF', 'PROK',
               'RXRX', 'SBLK', 'BWIN', 'STNG', 'PTY', 'NWL', 'MTRN', 'DEA']


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
