import pandas as pd
import matplotlib.pyplot as plt
import time

from log import Log
from request import get_mark_price
from event import chk_event_1, chk_event_2

print("### start server ###")

while True:
    response = get_mark_price('GODSUSDT')

    if response is None: continue

    else:
        if chk_event_1(response):
            Log("ET1", "알림발생", "GODSUSDT").lprint()
        if chk_event_2(response):
            Log("ET2", "알림발생", "GODSUSDT").lprint()

        df = response
        df.plot(x="time", y=["C", "50EMA", "100EMA"])
        df.plot(x="time", y=["CCI"])
        plt.show()

    time.sleep(60)