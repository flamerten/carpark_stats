from text_files import bot_token
from functions import *

from telegram.ext import *
from telegram import Update
import logging

def addcmd(text,func):
    handler = CommandHandler(text,func)
    dispatcher.add_handler(handler)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token = bot_token(),use_context = True)
dispatcher = updater.dispatcher

addcmd('start',start)
addcmd('find',get_carparks)
addcmd('help',help_text)


#for unknown commands
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()

#updater.stop() to close
