import requests

from config import WEBHOOK

discordwebhook = WEBHOOK

def send_msg(msg):
    data = {
        "content" : msg,
    }
    result = requests.post(discordwebhook, json=data)

