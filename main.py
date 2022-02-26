from text_files import bot_token
from bot_functions import *

from telegram.ext import *
from telegram import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ParseMode,
    ReplyKeyboardMarkup,
    KeyboardButton,
)

import logging


def addcmd(text,func):
    handler = CommandHandler(text,func)
    dispatcher.add_handler(handler)

def addfilter(filter,func):
    handler = MessageHandler(filter,func)
    dispatcher.add_handler(handler)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token = bot_token(),use_context = True)
dispatcher = updater.dispatcher

addcmd('start',start)
addcmd('help',help_text)

#filter for locations
addfilter(Filters.location,find_loc)

#for unknown commands
addfilter(Filters.command,unknown)
updater.start_polling()

#updater.stop() to close
