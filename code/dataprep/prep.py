df = pd.read_csv('../../data/raw/touch_events.csv')
df['time'] = pd.to_datetime(df['doc_created_utc_milli'])
df['time'] = df["time"].dt.strftime("%d/%m/%Y %H:%M:%S")
df.drop('doc_created_utc_milli', inplace=True, axis=1)
df.drop('event', inplace=True, axis=1)
df = df[['time', 'class']]
df.to_csv('../../data/processed/data_processed.csv')
print(df)