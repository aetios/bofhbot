import sys
from telegram.ext import Updater, CommandHandler
import excuses


def excuse(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=excuses.get_excuse())


telegram_api_key = sys.argv[1]
updater = Updater(token=telegram_api_key)
dispatcher = updater.dispatcher

excuse_handler = CommandHandler("excuse", excuse)

dispatcher.add_handler(excuse_handler)

updater.start_polling()
