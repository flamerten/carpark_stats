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
import parking_map

import io
from PIL import Image

from usage_functions import get_carpark_data

def start(update: Update, context: CallbackContext):
    location_keyboard = KeyboardButton(text="Send Location", request_location=True)
    reply_markup = ReplyKeyboardMarkup([[location_keyboard,]])
    context.bot.send_message(chat_id=update.effective_chat.id, text=start_text(), reply_markup=reply_markup)

def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid Command. Press /help for a list of commands")

def help_text(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_txt())

def find_loc(update: Update, context: CallbackContext):
    loc = update.message.location
    location = (loc.longitude,loc.latitude)
    print(location)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Your location is " + str(location))
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please wait 5s for the map to be generated")

    img_data = parking_map.generate_map(location,get_carpark_data())
    context.bot.send_photo(
        chat_id=update.effective_chat.id,
        caption = "This is the map",
        photo = img_data)
