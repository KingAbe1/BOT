from telegram.ext import *
from telegram.ext.dispatcher import run_async
from telegram import *


def language(update,context):
    keyboard = [['English', 'Amharic']]
    message = "Select a language / ቋንቋ ይምረጡ"
    reply_markup = ReplyKeyboardMarkup(keyboard,one_time_keyboard=True,resize_keyboard=True)
    update.message.reply_text(message, reply_markup=reply_markup)