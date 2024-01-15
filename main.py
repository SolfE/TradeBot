import pandas as pd
from pybit.unified_trading import HTTP
import matplotlib.pyplot as plt
from pprint import pprint
import time

def make_cci(high, low, close):
    m = (high + low + close) / 3
    n = m.rolling(20).mean()
    d = m.rolling(20).apply(lambda x : pd.Series(x).mad())
    cci = (m - n) / (0.015 * d)

    return cci

def make_ema(close, n):
    return close.ewm(span=n, adjust=False).mean()

# 5분마다 연산

session = HTTP(testnet=True)
response = session.get_mark_price_kline(
    category="linear",
    symbol="BTCUSDT",
    interval="D",
    limit = 200
)['result']['list']

response = response[::-1]

# 전처리 EMA, CCI

df = pd.DataFrame(response, columns=["time", "O", "H", "L", "C"])
df = df.astype(float)
df['CCI'] = make_cci(df["H"], df["L"], df["C"])
df['50EMA'] = make_ema(df["C"], 50)
df['100EMA'] = make_ema(df["C"], 100)
df.plot(x="time", y=["50EMA", "100EMA"])
plt.show()

print(df)