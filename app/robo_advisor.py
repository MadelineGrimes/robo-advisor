import os
from dotenv import load_dotenv
load_dotenv()

import requests

import pandas as pd
data = pd.read_table("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv")

response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv')

#Ensure we work with USD 
def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

#av_data = requests.get(data)
#Info Inputs

print("Requesting some data...")

#Note to self: Set up the logic BEFORE the API work! Plug this in last after the logic is verified to work. 

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
#Accept user input
symbol = input("Please enter a stock ticker: ")
request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"

if (symbol.isalpha) == False:
    print("Sorry, that's an invalid symbol.")
    exit()

response = requests.get(request_url)

#Need to access the keys within Time Series Daily

df = pd.DataFrame(data, columns= ['timestamp', 'open', 'high', 'low', 'close', 'volume'])

df.to_csv (r'C:\Users\madelinegrimes\Documents\GitHub\robo-advisor\export_dataframe.csv', index = False, header=True)

rows = []

latest_close = rows[0]['close']
high_prices = [row['high'] for row in rows] 
low_prices = [row['low'] for row in rows] 
recent_high = max(high_prices)
recent_low = min(low_prices)

import datetime
x = datetime.datetime.now ()


print (df)




#print(type(response))
#print(response.status_code)
#print(response.text)



#Info Outputs

print("-------------------------")
print("SELECTED SYMBOL: [symbol]")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: [x]")
print("-------------------------")
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: [latest_close]")
print("RECENT HIGH: [recent_high]")
print("RECENT LOW: [recent_low]")
print("-------------------------")

if latest_close > recent_high:
    print("RECOMMENDATION: Do not buy. This stock will soon lose value.")

if latest_close < recent_high:
    print("RECOMMENDATION: Buy! This stock will soon increase in value.")

print("-------------------------")
print("Happy investing! Thanks for stopping by.")
print("-------------------------")
