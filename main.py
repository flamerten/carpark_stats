from text_files import *
#from functions import Mainbot

from telegram.ext import *
from telegram import Update
import logging



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token = bot_token(),use_context = True)
dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=start_text())


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


updater.start_polling()

#updater.stop() to close
