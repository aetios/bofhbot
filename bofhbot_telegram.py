import sys
import random
import collections
from telegram.ext import Updater, CommandHandler

telegram_api_key = sys.argv[1]
updater = Updater(token=telegram_api_key)
dispatcher = updater.dispatcher


file = open("./excuses.txt")
content = [line.strip() for line in file.readlines()]
last60 = collections.deque([], 60)


def excuse(bot, update):
    while True:
        randomnr = random.randint(0, len(content))
        if randomnr not in last60:
            last60.append(randomnr)
            break

    bot.send_message(chat_id=update.message.chat_id, text=content[randomnr], parse_mode="markdown")


excuse_handler = CommandHandler("excuse", excuse)

dispatcher.add_handler(excuse_handler)

updater.start_polling()
