from datetime import datetime

class Log():
    def __init__(self, code, msg):
        self.time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.code = code
        self.msg = msg

    def lprint(self):
        print(f"[{self.time}] {self.code} : {self.msg}")