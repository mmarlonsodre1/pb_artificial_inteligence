import pandas as pd

df = pd.read_csv("./data/raw/touch_events.csv")
df['time'] = pd.to_datetime(df['doc_created_utc_milli'])
df['time'] = df["time"].dt.strftime("%Y-%m-%d %H:%M:%S")

df.drop('doc_created_utc_milli', inplace=True, axis=1)
df.drop('event', inplace=True, axis=1)
df = df[['time', 'class']]
df = df.set_index('time')
df['class'].mask(df['class'] == 'r', 0, inplace=True)
df['class'].mask(df['class'] == 'b', 1, inplace=True)
df['class'].mask(df['class'] == 'k', 2, inplace=True)
df.to_csv('./data/processed/touch_events.csv')