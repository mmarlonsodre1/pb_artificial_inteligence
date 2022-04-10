import math
import pandas as pd
import torch
from prophet import Prophet

torch.pi = math.pi
df = pd.read_csv('/Users/marlonsodre/Desktop/Develop.nosync/Python/pb_artificial_inteligence/data/modeling/data_model.csv')

df['ds'] = pd.to_datetime(df.ds)
df.set_index(df.ds.values, inplace=True)
df.sort_index(inplace=True)
df['y'] = df.topic
df.drop(['topic', '__dt'], axis=1, inplace=True)


m = Prophet()
m.fit(df)
future = m.make_future_dataframe(periods=30)
forecast = m.predict(future)

print(forecast.yhat.values)