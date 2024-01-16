# BYBIT 주가탐색 알림봇

## 소개

인기있는 암호화폐 거래를 직접 검사하는 것은 귀찮은 일이다. 따라서 이를 해결하보고자 BYBIT와 DISCORD API를 엮어 원하는 주가에 원하는 이벤트가 발생하면 DISCORD로 알림을 보내주는 프로그램이다.

## 사용법
1. python 3.9버전을 설치한다.
2. config.py를 원하는 설정값에 맞춰 수정한다.
```python
# config.py
# 환경변수 자유롭게 수정하여 사용

WEBHOOK = "PUT_IN_YOUR_DISCORD_WEB_HOOK"
SYMBOL_LIST = [
    'BTCUSDT',
    'ETHUSDT',
]
GET_ALL_SYMBOL = True
SERVER_INTERVAL = 60 # sec
CANDLE_INTERVAL = 1 # min
```
3. 패키지를 설치한다.
    > $ pip install -r requirements.txt
4. main.py를 실행한다.
    > $ python main.py