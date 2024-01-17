import matplotlib.pyplot as plt
from pybit.unified_trading import HTTP
import time

from log import Log
from request import get_mark_history
from event import chk_event_1, chk_event_2
from discordAPI import send_msg
from pay import buy_market_price, sell_market_price
from config import SYMBOL_LIST, SERVER_INTERVAL, GET_ALL_SYMBOL, TEST_NET

print("######### start server #########")

if GET_ALL_SYMBOL:
    session = HTTP(testnet=TEST_NET)
    SYMBOL_LIST = list(map(lambda x : x['symbol'], session.get_tickers(category="linear")['result']['list']))

print(f"SYMBOLS : {SYMBOL_LIST}")
print(f"SYMBOLS_COUNT : {len(SYMBOL_LIST)}")

while True:
    for symbol in SYMBOL_LIST:
        response = get_mark_history(symbol)

        if response is None: continue

        else:
            if chk_event_1(response):
                log = Log("골크", "롱", symbol)
                log.lprint()
                send_msg(log.get())
            if chk_event_2(response):
                log = Log("데드", "숏", symbol)
                log.lprint()
                send_msg(log.get())

            # df = response
            # df.plot(x="time", y=["C", "50EMA", "100EMA"])
            # df.plot(x="time", y=["CCI"])
            # plt.show()
            # print(df)

    time.sleep(SERVER_INTERVAL)