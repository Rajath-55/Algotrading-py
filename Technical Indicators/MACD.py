import numpy as np
import pandas as pd
import datetime as dt
from pandas_datareader import data

df = pd.DataFrame()
df = data.DataReader('AMZN', 'yahoo', start = dt.date.today() - dt.timedelta(144))
df = df.head(144)

def MACD(Df, a, b, c):
    df = Df.copy()
    df['MA_Fast'] = df['Adj Close'].ewm(span = a, min_periods = a).mean()
    df['MA_Slow'] = df['Adj Close'].ewm(span = b, min_periods = b).mean()
    df['MACD'] = df['MA_Fast'] - df['MA_Slow']
    df['Signal'] = df['MACD'].ewm(span = c, min_periods = c).mean()
    df.dropna(inplace = True)
    return df

print(MACD(df, 12, 26, 14))