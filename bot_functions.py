#to be implemented
from telegram.ext import *
from telegram import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ParseMode,
    ReplyKeyboardMarkup,
    KeyboardButton,
    Update
)
from text_files import *

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=start_text())

def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid Command. Press /help for a list of commands")

def help_text(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_txt())

def find_loc(update: Update, context: CallbackContext):
    loc = update.message.location
    location = (loc.longitude,loc.latitude)
    print(location)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Your location is " + str(location))