import numpy as np
import pandas as pd
import datetime as dt
from pandas_datareader import data
import matplotlib.pyplot as plt

df = pd.DataFrame()
df = data.DataReader('AMZN', 'yahoo', start = dt.date.today() - dt.timedelta(144))['Adj Close']
df = df.head(144)

price_max = df.max()
price_min = df.min()
diff = price_max - price_min
level1 = price_max - 0.236 * diff
level2 = price_max - 0.382 * diff
level3 = price_max - 0.618 * diff

print ("Level", "Price")
print ("0    ", price_max)
print ("0.236", level1)
print ("0.382", level2)
print ("0.618", level3)
print ("1    ", price_min)

fig, ax = plt.subplots()
ax.plot(df, color='black')
ax.axhspan(level1, price_min, alpha=0.4, color='lightsalmon')
ax.axhspan(level2, level1, alpha=0.5, color='palegoldenrod')
ax.axhspan(level3, level2, alpha=0.5, color='palegreen')
ax.axhspan(price_max, level3, alpha=0.5, color='powderblue')

plt.ylabel("Price")
plt.xlabel("Date")
plt.legend(loc = 2)
plt.show()