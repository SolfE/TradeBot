from pybit.unified_trading import HTTP
import pandas as pd

from log import Log

def make_cci(high, low, close):
    m = (high + low + close) / 3
    n = m.rolling(20).mean()
    d = m.rolling(20).apply(lambda x : (x - x.mean()).abs().mean())
    cci = (m - n) / (0.015 * d)

    return cci

def make_ema(close, n):
    return close.ewm(span=n, adjust=False).mean()

def get_mark_price(symbol):
    session = HTTP(testnet=True)
    response = session.get_mark_price_kline(
        symbol = symbol,
        interval = 1,
        limit = 200
    )
    response_code = response["retCode"]
    if response_code == 0: Log("200", "OK").lprint()
    else:
        Log("400", "Fail to Get DATA").lprint()
        return None
    response = response['result']['list']
    response = response[::-1]

    # 전처리
    df = pd.DataFrame(response, columns=["time", "O", "H", "L", "C"])
    df = df.astype(float)

    # EMA CCI 추가
    df['CCI'] = make_cci(df["H"], df["L"], df["C"])
    df['50EMA'] = make_ema(df["C"], 50)
    df['100EMA'] = make_ema(df["C"], 100)

    df = df.loc[::-1].reset_index(drop=True)

    return df