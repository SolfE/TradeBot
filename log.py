from datetime import datetime
class Log():
    def __init__(self, code, msg, symbol):
        self.time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.code = code
        self.msg = msg
        self.symbol = symbol

    def lprint(self):
        print(f"[{self.time}][{self.symbol}] {self.code} : {self.msg}")
    def get(self):
        return f"[{self.time}][{self.symbol}] {self.code} : {self.msg}"