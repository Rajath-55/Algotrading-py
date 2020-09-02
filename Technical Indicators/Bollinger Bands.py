import numpy as np
import pandas as pd
import datetime as dt
from pandas_datareader import data

df = pd.DataFrame()
df = data.DataReader('AMZN', 'yahoo', start = dt.date.today() - dt.timedelta(144))
df = df.head(144)

def BollBnd(Df, n):
    df = Df.copy()
    df['MA'] = df['Adj Close'].rolling(n).mean()
    df['BB_up'] = df['Adj Close'].rolling(n).mean() + 2*df['MA'].rolling(n).std()
    df['BB_dn'] = df['Adj Close'].rolling(n).mean() - 2*df['MA'].rolling(n).std()
    df['BB_Width'] = df['BB_up'] - df['BB_dn']
    df.dropna(inplace = True)
    return df

print(BollBnd(df, 14))