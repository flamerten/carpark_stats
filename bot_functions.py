#to be implemented
from telegram.ext import *
from telegram import Update
from text_files import *

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=start_text())

def get_carparks(update: Update, context: CallbackContext):
    """Get postal code of nearest place, and print it back - for further dev"""
    postal_code = ' '.join(context.args)
    if len(postal_code) != 6:
        msg = "Your postal code is invalid, try again"
    else:
        msg = "Valid Postal Code \nYour Postal Code is " + postal_code

    context.bot.send_message(chat_id=update.effective_chat.id, text=msg )

def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid Command. Press /help for a list of commands")

def help_text(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_txt())
