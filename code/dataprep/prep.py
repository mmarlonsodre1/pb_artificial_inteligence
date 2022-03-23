import pandas as pd

df = pd.read_csv("/Users/marlonsodre/Desktop/Develop.nosync/Python/pb_artificial_inteligence/data/raw/touch_events.csv")
df['time'] = pd.to_datetime(df['doc_created_utc_milli'])
df['time'] = df["time"].dt.strftime("%d/%m/%Y %H:%M:%S")

df.drop('doc_created_utc_milli', inplace=True, axis=1)
df.drop('event', inplace=True, axis=1)
df = df[['time', 'class']]
df = df.set_index('time')
df.to_csv('/Users/marlonsodre/Desktop/Develop.nosync/Python/pb_artificial_inteligence/data/processed/touch_events.csv')