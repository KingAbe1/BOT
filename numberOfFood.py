from telegram.ext import *
from telegram.ext.dispatcher import run_async
from telegram import *


def numberoffood(update,context):
    keyboard = [['yes', 'no']]
    message = "Do you want to additional order?"
    reply_markup = ReplyKeyboardMarkup(keyboard,one_time_keyboard=True,resize_keyboard=True)
    update.message.reply_text(message, reply_markup=reply_markup)

def numberoffoodAmharic(update,context):
    keyboard = [['አዎ', 'አይ']]
    message = "ተጨማሪ ትዕዛዝ ይፈልጋሉ?"
    reply_markup = ReplyKeyboardMarkup(keyboard,one_time_keyboard=True,resize_keyboard=True)
    update.message.reply_text(message, reply_markup=reply_markup)