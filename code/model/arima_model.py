from pmdarima import auto_arima
import pandas as pd
from pmdarima.arima.stationarity import ADFTest
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv(
    './data/modeling/data_model.csv'
)

df['ds'] = pd.to_datetime(df.ds)
df.set_index(df.ds.values, inplace=True)
df.sort_index(inplace=True)
df['y'] = df.topic
df.drop(['topic', '__dt', 'ds'], axis=1, inplace=True)

adf = ADFTest()
print(adf.is_stationary(df))

size_of_train = int(np.ceil(df.shape[0] * 0.75))
train = df.iloc[:size_of_train]
test = df.iloc[size_of_train:]

model = auto_arima(
    train,
    start_p=1,
    start_q=1,
    max_p=8,
    max_q=8,
    m=12,
    d=1,
    D=1,
    seasonal=True,
    stepwise=False,
    random_state=20,
    n_fits=30
)

model.fit(train)
forecast = model.predict(n_periods=len(test))
forecast = pd.Series(forecast, index=test.index)

fig, ax = plt.subplots(1, 1, figsize=(20, 6))
train.plot(ax=ax)
test.plot(ax=ax, c="g")
forecast.plot(ax=ax, c="r", ls=":")

ax.yaxis.grid(True)
ax.legend(["Treino", "Teste", "Predição"])
plt.show()
