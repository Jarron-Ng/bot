from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler
from time import sleep
import logging
import requests
url = "https://api.telegram.org/bot455857878:AAGzjdOvmz21WMGffkGbChCGPkfxriXFbXE/"
updater = Updater(token='455857878:AAGzjdOvmz21WMGffkGbChCGPkfxriXFbXE')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    y = bot.send_message(chat_id=update.message.chat_id, text="lynch chicole nong")
    print(y)

start_handler = CommandHandler('speak', start)
dispatcher.add_handler(start_handler)

def talk(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="ProGene carry me to GM")

start_handler = CommandHandler('talk', talk)
dispatcher.add_handler(start_handler)

def call(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="git gud aqua sissy")

start_handler = CommandHandler('aqua', call)
dispatcher.add_handler(start_handler)

def sing(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="faded by beatbox")

start_handler = CommandHandler('sing', sing)
dispatcher.add_handler(start_handler)

def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
         InlineQueryResultArticle(
             id=query.upper(),
             title='Caps',
             input_message_content=InputTextMessageContent(query.upper())
         )
    )
    bot.answer_inline_query(update.inline_query.id, results)

inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)


updater.start_polling()

