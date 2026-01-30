# https://www.geeksforgeeks.org/python/build-a-gui-application-to-get-live-stock-price-using-python/
# Import the Required modules
import yfinance as yf
#https://pythonfintech.com/articles/how-to-download-market-data-yfinance-python/
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#import configparser
#import seaborn as sns

# Inputting the name of the Stock and Storing it in a Variable
#STK = input("Enter share name : ")
#STK = "AAPL"
#STK = "TRN.MI"
#STK="MSFT"
STK="QQQ"
STK1=""
STK2=""
STK3=""
myperiod = "5y"
fromYear=2021
fromMonth=1
fromDay=27
#https://codesignal.com/learn/courses/fundamentals-of-text-data-manipulation/lessons/parsing-files-line-by-line-in-python


mydir='C:\\Users\\grippst1\\source\\repos\\python\\'
file_path =  mydir + 'settings.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()
    
for line in lines:
    if (line.find("Symbol=")>= 0):
        STK=line[7:]
        STK = STK.replace("\n", "")
    if (line.find("Symbol1=")>= 0):
        if (len(line) > 9):
            print("symbol1 found length =", len(line))
            STK1=line[8:]
            STK1 = STK1.replace("\n", "") 
    if (line.find("Symbol2=")>= 0):
        if (len(line) > 9):
            print("symbol2 found")
            STK2=line[8:]
            STK2 = STK2.replace("\n", "")  
    if (line.find("Symbol3=")>= 0):
        if (len(line) > 9):
            print("symbol3 found")
            STK3=line[8:]
            STK3 = STK3.replace("\n", "")                    
    if (line.find("fromYear=")>= 0):
        fromYear=line[8:]
        fromYear = fromYear.replace("\n", "")
    if (line.find("fromMonth=")>= 0):
        fromMonth=line[9:]   
        fromMonth = fromMonth.replace("\n", "")
    if (line.find("fromDay=")>= 0):
        fromDay=line[7:]
        fromDay = fromDay.replace("\n", "")
    if (line.find("period=")>= 0):
        myperiod=line[7:] 
        myperiod = myperiod.replace("\n", "")
# lo leggo dal file di impostazioni
#file= 'C:\\Users\\grippst1\\source\\repos\\python\\settings.txt'
#config = configparser.ConfigParser(file)
#config.read("settings.txt")
#config.get('default','fromYear')
#fromYear = config['DEFAULT']['fromYear']
#fromMonth = config['DEFAULT']['fromMonth']
#fromDay = config['DEFAULT']['fromDay']
#STK = config['DEFAULT']['Symbol']
# Extract the Share information using the Ticker() Function
Share = yf.Ticker(STK).info

MyISIN = yf.Ticker(STK).isin
#Dividends = yf.Ticker(STK).get_dividends()

# Extracting the MarketPrice from the data
#market_price = Share['regularMarketPrice' ]
#current_price = Share['current_price']
#last_price = Share['last_price']

# Printing the market price
#print("market price = ", market_price)

#print("last price = ", last_price)
print ("ISIN =", MyISIN)

#data = yf.download(STK, start="2026-01-01", end="2026-01-23")

#data = yf.download(STK, period=myperiod)
#print(pd.DataFrame(data))
#pd.DataFrame(data).plot(style='.-')

listoftickers = []
if not STK:
    print ("ticker is null")
else:
    listoftickers.append(STK)



if not STK1:
    print ("ticker 1 is null")
else:
    listoftickers.append(STK1)

if not STK2:
    print ("ticker 2 is null")
else:
    listoftickers.append(STK2)

if not STK3:
    print ("ticker 3 is null")
else:
    listoftickers.append(STK3)


print ("list of tickers =", listoftickers)
for ticker in listoftickers:
    data = yf.download(ticker, period=myperiod)
    pd.DataFrame(data).to_csv(mydir + ticker + "_" + myperiod + ".csv")  
    MyISIN = yf.Ticker(ticker).isin
    print ("for ticker ", ticker, " ISIN =", MyISIN)
    
#x = [10, 20, 30, 40, 50, 60]
#y = [13, 45, 23, 34, 96, 76]
#plt.title('Bar Graph')
#plt.bar(x, y, color='dodgerblue', width=5)
#plt.show()

 
#pd.DataFrame(data).plot.line()


#x = np.linspace(0, 20, 100)
#plt.plot(x, np.sin(x))
#plt.show()

#miaLista = data.to_numpy().tolist()
#https://www.reddit.com/r/learnpython/comments/10adfru/yfinance_getting_price_data/?tl=it
#MyClosedata = data['Close'].values.to_list()
#data = yf.download("MSFT", period="1y")
# data.boxplot()


#This Code is Contributed by PL VISHNUPPRIYANAMZN