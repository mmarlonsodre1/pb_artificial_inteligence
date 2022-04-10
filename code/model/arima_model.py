from pmdarima import auto_arima
import pandas as pd
from pmdarima.arima.stationarity import ADFTest

df = pd.read_csv(
    '/Users/marlonsodre/Desktop/Develop.nosync/Python/pb_artificial_inteligence/data/modeling/data_model.csv'
)

df['ds'] = pd.to_datetime(df.ds)
df.set_index(df.ds.values, inplace=True)
df.sort_index(inplace=True)
df['y'] = df.topic
df.drop(['topic', '__dt', 'ds'], axis=1, inplace=True)

adf = ADFTest()
print(adf.is_stationary(df))

model = auto_arima(
    df,
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
model.fit(df)
forecast = model.predict(n_periods=30)
print(forecast)
