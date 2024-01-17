from config import API_SECRET, API_KEY, LEVERAGE, TEST_NET, CANDLE_INTERVAL
from log import Log
from discordAPI import send_msg

from pybit.unified_trading import HTTP

def get_market_price(symbol):
    session = HTTP(testnet=TEST_NET)
    try:
        return float(session.get_mark_price_kline(
            category="linear",
            symbol=symbol,
            interval=CANDLE_INTERVAL,
            limit=1,
        )['result']['list'][0][4])
    except:
        return None

def buy_market_price(symbol, price, take_profit, stop_loss):
    market_price = get_market_price(symbol)

    if market_price is None:
        log = Log("400", "BUY FAIL", symbol)
        log.lprint()
        return
    qty = str(price // market_price)

    session = HTTP(
        testnet=TEST_NET,
        api_key=API_KEY,
        api_secret=API_SECRET,
    )

    try:
        session.set_leverage(
            category="linear",
            symbol=symbol,
            buyLeverage=LEVERAGE,
            sellLeverage=LEVERAGE,
        )
    except:
        pass

    try:
        session.place_order(
            category="linear",
            symbol=symbol,
            side="Buy",
            orderType="Market",
            qty=qty,
            takeProfit = take_profit,
            stopLoss = stop_loss,
            timeInForce="PostOnly",
            isLeverage=1,
            orderFilter="Order",
        )
        log = Log("200", f"BUY price:{price} qty:{qty}", symbol)
        log.lprint()
        send_msg(log.get())
    except:
        log = Log("400", "BUY FAIL", symbol)
        log.lprint()

def sell_market_price(symbol, price, take_profit, stop_loss):
    market_price = get_market_price(symbol)

    if market_price is None:
        log = Log("400", "BUY FAIL", symbol)
        log.lprint()
        return
    qty = str(price // market_price)

    session = HTTP(
        testnet=TEST_NET,
        api_key=API_KEY,
        api_secret=API_SECRET,
    )

    try:
        session.set_leverage(
            category="linear",
            symbol=symbol,
            buyLeverage=LEVERAGE,
            sellLeverage=LEVERAGE,
        )
    except:
        pass

    try:
        session.place_order(
            category="linear",
            symbol=symbol,
            side="Sell",
            orderType="Market",
            qty=qty,
            takeProfit = take_profit,
            stopLoss = stop_loss,
            # price="42930",
            timeInForce="PostOnly",
            # orderLinkId="spot-test-postonly",
            isLeverage=1,
            orderFilter="Order",
        )

        log = Log("200", f"SELL price:{price} qty:{qty}", symbol)
        log.lprint()
        send_msg(log.get())
    except:
        log = Log("400", "SELL FAIL", symbol)
        log.lprint()