import pandas as pd 
import pandas_datareader as pdr 
import datetime
aapl = pdr.get_data_yahoo('AAPL', start=datetime.datetime(2008,1,1), end=datetime.datetime(2012,1,1))
print(aapl.describe())
aapl.to_csv('aapl_02_04.csv')
download_aapl = "02_04CSV.csv"

aapl['Change'] = aapl.Open - aapl.Close
aapl['Pct_Chg'] = aapl.Change/aapl.Open

import matplotlib.pyplot as plt

aapl['Pct_Chg'].plot(grid=True)
# plt.show()

def get(tickers, startdate, enddate):
    def data(ticker):
        return(pdr.get_data_yahoo(ticker, start=startdate, end=enddate))
    datas = map(data, tickers)
    return(pd.concat(datas, keys=tickers, names=['Ticker', 'Date']))
tickers = ['MSFT', 'CRM', 'GE', 'MMM']

all_data = get(tickers, datetime.datetime(2015,1,1), datetime.datetime(2019,1,1))
print(all_data.describe())