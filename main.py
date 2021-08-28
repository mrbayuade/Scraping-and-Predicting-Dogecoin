"""
First, I want to scrap historical data of Dogecoin in website https://coinmarketcap.com/.
The data contains open,high,low,and close price of Dogecoin, then I want to predict
close price of Dogecoin in the future using historical data.
In this project I use library in python :
1. cryptocmd : to scrap historical data of a cryptocurrency in https://coinmarketcap.com/
2. fbprophet : a procedure for forecasting time series data based on an additive model
               where non-linear trends are fit with yearly, weekly, and daily seasonality,
               plus holiday effects.
source : https://pypi.org/
"""

# Data Scraping
from cryptocmd import CmcScraper
scraper = CmcScraper("DOGE")
headers, data = scraper.get_data()
xrp_json_data = scraper.get_data("json")
df = scraper.get_dataframe()

# Data Preparation
df[["ds","y"]] = df[["Date","Close"]]
df.describe()

# Data Analysis
# from fbprophet import Prophet
# model = Prophet()
# model = model.fit(df)
# future   = model.make_future_dataframe(periods=365)
# forecast = model.predict(future)
# print(forecast)

print(df)

