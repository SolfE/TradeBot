import matplotlib.pyplot as plt
from pybit.unified_trading import HTTP
import time
from pprint import pprint

from log import Log
from request import get_mark_price
from event import chk_event_1
from discordAPI import send_msg
from config import SYMBOL_LIST, SERVER_INTERVAL, GET_ALL_SYMBOL

print("######### start server #########")

if GET_ALL_SYMBOL:
    session = HTTP(testnet=True)
    SYMBOL_LIST = list(map(lambda x : x['symbol'], session.get_tickers(category="spot")['result']['list']))

pprint(f"SYMBOLS : {SYMBOL_LIST}")
print(f"SYMBOLS_COUNT : {len(SYMBOL_LIST)}")

while True:
    for symbol in SYMBOL_LIST:
        response = get_mark_price(symbol)

        if response is None: continue

        else:
            if chk_event_1(response):
                log = Log("ET1", "알림발생", symbol)
                log.lprint()
                send_msg(log.get())
            # if chk_event_2(response):
            #     log = Log("ET2", "알림발생", symbol)
            #     log.lprint()
            #     send_msg(log.get())

            # df = response
            # df.plot(x="time", y=["C", "50EMA", "100EMA"])
            # df.plot(x="time", y=["CCI"])
            # plt.show()
    time.sleep(SERVER_INTERVAL)