# Scraping-and-Predicting-Dogecoin

First, I want to scrap historical data of Dogecoin in website https://coinmarketcap.com/.
The data contains open,high,low,and close price of Dogecoin, then I want to predict
close price of Dogecoin in the future using historical data.
In this project I use library in python :
1. cryptocmd : to scrap historical data of a cryptocurrency in https://coinmarketcap.com/
2. fbprophet : a procedure for forecasting time series data based on an additive model
               where non-linear trends are fit with yearly, weekly, and daily seasonality,
               plus holiday effects.
source : https://pypi.org/


# Conclusion
The historical data of Dogecoin is from  2013-04-28 until 2021-08-27,
because in this project I scrap the data on 2021-08-29 and data in website
always update everyday so does the scraper. You can see the codes
on main.py file.
Based on results I can conclude that :
1. Based on trend Dogecoin close price will significantly increase for next year.
2. Based on weekly I can see the lowest close price is on tuesday and the higgest is on friday.
3. Based on yearly, the lowest close price is on april and december, and the highest is on may. 