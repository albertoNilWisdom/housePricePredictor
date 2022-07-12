
#sauce https://www.viralml.com/video-content.html?v=AX1wKnBPhvU
import time
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import io, base64, os, json, re, glob
import datetime
from datetime import timedelta
import pandas as pd
import pydata_google_auth
import numpy as np
from fbprophet import Prophet
df_raw = pd.read_csv('/home/ted/Documents/Programming/datasets/gov-paid-prices-housing/currentSearch.csv',
                     low_memory=False,
                     parse_dates=['DateArrived'],
                     index_col=['DateArrived'])
df_raw = df_raw.sort_values('DateArrived', ascending=True)
print(df_raw.shape)
df_raw.head()

# plt.subplots(1,figsize=(16,5))
# plt.grid()
# plt.title('ReferralDemand')
# for data in set(df_raw['ID']):
#     plt.plot((df_raw['ID']==20)['Sum'].rolling(window=1).mean()) 
# plt.subplots(1,figsize=(16,5))
# plt.grid()
# plt.title('Ref Demand')
# for ID in set(df_raw[df_raw['ID'] ==4]['ID']):
#     plt.plot((df_raw['ID']==ID)]['Sum'].rolling(window=1).mean())

## TRAIN ON DATA
# preparing the data into FBP format:
train_dataset = df_raw[df_raw['ID'] == 22] ####<<<---the caseloadID
train_dataset.reset_index(level=0, inplace=True)

train_dataset = train_dataset[['DateArrived', 'Sum']]

train_dataset.columns = ["ds", "y"]
#train_dataset = train_dataset.sample(500)
prophet_basic = Prophet(yearly_seasonality=True)
prophet_basic.fit(train_dataset)

horizon = 365
future = prophet_basic.make_future_dataframe(import time
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import io, base64, os, json, re, glob
import datetime
from datetime import timedelta
import pandas as pd
import pydata_google_auth
import numpy as np
from fbprophet import Prophet
df_raw = pd.read_csv('ReferralDemand2014-2018.csv',
                     low_memory=False,
                     parse_dates=['DateArrived'],
                     index_col=['DateArrived'])
df_raw = df_raw.sort_values('DateArrived', ascending=True)
print(df_raw.shape)
df_raw.head()

# plt.subplots(1,figsize=(16,5))
# plt.grid()
# plt.title('ReferralDemand')
# for data in set(df_raw['ID']):
#     plt.plot((df_raw['ID']==20)['Sum'].rolling(window=1).mean())
# plt.subplots(1,figsize=(16,5))
# plt.grid()
# plt.title('Ref Demand')
# for ID in set(df_raw[df_raw['ID'] ==4]['ID']):
#     plt.plot((df_raw['ID']==ID)]['Sum'].rolling(window=1).mean())

## TRAIN ON DATA
# preparing the data into FBP format:
train_dataset = df_raw[df_raw['ID'] == 22] ####<<<---the caseloadID
train_dataset.reset_index(level=0, inplace=True)

train_dataset = train_dataset[['DateArrived', 'Sum']]

train_dataset.columns = ["ds", "y"]
#train_dataset = train_dataset.sample(500)
prophet_basic = Prophet(yearly_seasonality=True)
prophet_basic.fit(train_dataset)

horizon = 365
future = prophet_basic.make_future_dataframe(
    periods=horizon,
    freq='B' ##B stands for business days
)

#future= prophet_basic.make_future_dataframe(periods=365)
future

forecast=prophet_basic.predict(future)

#Plotting the predicted data
forecast=prophet_basic.predict(future)

#Plotting the predicted data
fig1 = prophet_basic.plot(forecast)

fig1 = prophet_basic.plot_components(forecast)
from fbprophet.plot import add_changepoints_to_plot
fig = prophet_basic.plot(forecast)
a = add_changepoints_to_plot(fig.gca(), prophet_basic, forecast)
forecast.to_csv('PredictOutput2019.csv')


    periods=horizon,
    freq='B' ##B stands for business days
)

#future= prophet_basic.make_future_dataframe(periods=365)
future

forecast=prophet_basic.predict(future)

#Plotting the predicted data
forecast=prophet_basic.predict(future)

#Plotting the predicted data
fig1 = prophet_basic.plot(forecast)

fig1 = prophet_basic.plot_components(forecast)
from fbprophet.plot import add_changepoints_to_plot
fig = prophet_basic.plot(forecast)
a = add_changepoints_to_plot(fig.gca(), prophet_basic, forecast)
forecast.to_csv('PredictOutput2019.csv')




#'/home/ted/Documents/Programming/datasets/gov-paid-prices-housing/currentSearch.csv'