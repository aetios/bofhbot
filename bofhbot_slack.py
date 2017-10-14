import sys
from slacker import Slacker
import websocket
import ssl
import json
import collections
import random

slack_api_key = sys.argv[1]
slack = Slacker(slack_api_key)

weburl = slack.rtm.start().body['url']
socket = websocket.create_connection(weburl, sslopt={"cert_reqs": ssl.CERT_NONE})

file = open("./excuses.txt")
content = [line.strip() for line in file.readlines()]
last60 = collections.deque([], 60)


def excuse():
    while True:
        randomnr = random.randint(0, len(content))
        if randomnr not in last60:
            last60.append(randomnr)
            break
    return content[randomnr]


def sendmessage(channel, text, socket):
    payload = json.JSONEncoder().encode({"id": 1, "type": "message", "channel": channel, "text":text})
    socket.send(payload)


while True:
    update = socket.recv()
    update = json.JSONDecoder().decode(update)
    if update.get('text') == '!excuse':
        sendmessage(update['channel'], excuse(), socket)

