import math
import pandas as pd
import torch
from prophet import Prophet
import numpy as np
from matplotlib import pyplot as plt

torch.pi = math.pi
df = pd.read_csv('./data/modeling/data_model.csv')

df['ds'] = pd.to_datetime(df.ds)
df.set_index(df.ds.values, inplace=True)
df.sort_index(inplace=True)
df['y'] = df.topic
df.drop(['topic', '__dt'], axis=1, inplace=True)

size_of_train = int(np.ceil(df.shape[0] * 0.75))
train = df.iloc[:size_of_train]
test = df.iloc[size_of_train:]

m = Prophet()
m.fit(train)
forecast = m.predict(test)

test.drop(['ds'], axis=1, inplace=True)
train.drop(['ds'], axis=1, inplace=True)
test['yhat'] = forecast.yhat.values
fig, ax = plt.subplots(1, 1, figsize=(20, 6))
train.plot(ax=ax)
test.plot(ax=ax, c="g")
ax.yaxis.grid(True)
plt.show()