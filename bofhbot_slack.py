import sys
from slacker import Slacker
import websocket
import ssl
import json
import excuses

slack_api_key = sys.argv[1]
slack = Slacker(slack_api_key)

weburl = slack.rtm.start().body['url']
socket = websocket.create_connection(weburl, sslopt={"cert_reqs": ssl.CERT_NONE})


def sendmessage(channel, text, socket):
    payload = json.JSONEncoder().encode({"id": 1, "type": "message", "channel": channel, "text":text})
    socket.send(payload)


while True:
    update = socket.recv()
    update = json.JSONDecoder().decode(update)
    if update.get('text') == '!excuse':
        sendmessage(update['channel'], excuses.get_excuse(), socket)

