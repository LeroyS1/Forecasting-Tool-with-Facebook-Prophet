
# how to install fbprophet for python
# First, open the MacOS terminal, then run the following commands:
# $ pip install pystan
# $ pip install fbprophet
# $ pip install plotly

from fbprophet import Prophet
import numpy as np
import pandas as pd
import sys
from fbprophet.plot import plot_plotly
import plotly.offline as py

# read in file
unemployment = pd.read_csv('unemployment_nolast12mo.csv')


df = pd.DataFrame()
df.reset_index(drop=True)
df['ds'] = unemployment['DATE']
df['y'] = unemployment['UNRATE']


m = Prophet(yearly_seasonality=False,
            weekly_seasonality=False,
            daily_seasonality=False,
            holidays=None,
            seasonality_mode='multiplicative',
            mcmc_samples=0).fit(df)
future = m.make_future_dataframe(periods=12, freq='MS')
future.tail()
forecast = m.predict(future)


# this line will cut down columns in the data frame.
# Now we can only see these columns: 'ds', 'yhat', 'yhat_lower', 'yhat_upper'.
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()


# these lines will write all the forecast results to a file called "data.txt."
# Note: if you run different datasets, you need to replace the filename"data.txt" with other names like "data1.txt" or any.
# Otherwise, it will overwrite the new results to the old one.
with open('data.txt', 'w') as f:
    print(forecast.to_string(), file=f)


fig1 = m.plot(forecast)
fig2 = m.plot_components(forecast)

fig = plot_plotly(m, forecast)  # This returns a plotly Figure
py.plot(fig)
