import os
from dotenv import load_dotenv
load_dotenv()
import requests

import pandas as pd
train = pd.read_table("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv")
train.head()

#Info Inputs

print("Requesting some data...")

#Note to self: Set up the logic BEFORE the API work! Plug this in last after the logic is verified to work. 

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
symbol = input("Please enter a stock ticker")

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"
print("URL:", request_url)

if (symbol.isalpha) == False:
    print("Sorry, that's an invalid symbol.")
    exit()

response = requests.get(request_url)

#print(type(response))
#print(response.status_code)
#print(response.text)



#Info Outputs

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
