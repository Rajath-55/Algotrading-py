import numpy as np
import pandas as pd
import datetime as dt
from pandas_datareader import data

df = pd.DataFrame()
df = data.DataReader('AMZN', 'yahoo', start = dt.date.today() - dt.timedelta(144))
df = df.head(144)

def ATR(Df, n):
    df = Df.copy()
    df['H-L']  = abs(df['High'] - df['Low'])
    df['H-PC'] = abs(df['High'] - df['Adj Close'].shift(1))
    df['L-PC'] = abs(df['Low'] - df['Adj Close'].shift(1))
    df['TR']  = df[['H-L', 'H-PC', 'L-PC']].max(axis = 1, skipna = False)
    df['ATR'] = df['TR'].rolling(n).mean()
    df2 = df.drop(['H-L', 'H-PC', 'L-PC'], axis = 1)
    return df2

print(ATR(df, 14))