import matplotlib.pyplot as plt
import time

from log import Log
from request import get_mark_price
from event import chk_event_1, chk_event_2
from discordAPI import send_msg
from config import SYMBOL_LIST, SERVER_INTERVAL

print("######### start server #########")
print(f"SYMBOLS : {SYMBOL_LIST}")

while True:
    for symbol in SYMBOL_LIST:
        response = get_mark_price(symbol)

        if response is None: continue

        else:
            if chk_event_1(response):
                log = Log("ET1", "알림발생", symbol)
                log.lprint()
                send_msg(log.get())
            if chk_event_2(response):
                log = Log("ET2", "알림발생", symbol)
                log.lprint()
                send_msg(log.get())

            # df = response
            # df.plot(x="time", y=["C", "50EMA", "100EMA"])
            # df.plot(x="time", y=["CCI"])
            # plt.show()
    time.sleep(SERVER_INTERVAL)