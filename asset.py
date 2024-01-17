from pybit.unified_trading import HTTP

from config import TEST_NET, API_KEY, API_SECRET
from log import Log

session = HTTP(
    testnet=TEST_NET,
    api_key=API_KEY,
    api_secret=API_SECRET,
)

def get_coin_wallet_balance(symbol):
    try:
        return float(session.get_coins_balance(
            accountType="UNIFIED",
            coin=symbol,
        )['result']['balance'][0]['transferBalance'])
    except:
        Log("400", "자산조회 실패", symbol).lprint()
