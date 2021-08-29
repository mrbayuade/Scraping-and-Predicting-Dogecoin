# Data Scraping
from cryptocmd import CmcScraper
scraper = CmcScraper("DOGE")
headers, data = scraper.get_data()
doge_json_data = scraper.get_data("json")
df = scraper.get_dataframe()

# Data Preparation
df[["ds","y"]] = df[["Date","Close"]]
df.describe()

# Data Analysis
from fbprophet import Prophet
import matplotlib.pyplot as plt
model = Prophet()
model = model.fit(df)
future = model.make_future_dataframe(periods=365)
forecast = model.predict(future)

# Data Visualization
ax = (df.plot(x='ds',y='y',figsize=(15,5),title='Actual Vs Forecast'))
forecast.plot(x='ds',y='yhat',figsize=(15,5),title='Actual vs Forecast', ax=ax)
model.plot(forecast)
model.plot_components(forecast)
plt.show()
