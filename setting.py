from telegram.ext import *
from telegram.ext.dispatcher import run_async
from telegram import *
import DatabaseConnector as db


def setting(update,context):
    keyboard = [['Change language to Amharic'],['Change Name'],['Back']]
    message = "⚙️Setting"
    reply_markup = ReplyKeyboardMarkup(keyboard,one_time_keyboard=True,resize_keyboard=True)
    update.message.reply_text(message, reply_markup=reply_markup)


def settingAmharic(update,context):
    keyboard = [['ቋንቋውን ወደ እንግሊዝኛ ይለውጡ'],['ስም ቀይር'],['ተመለስ']]
    message = "⚙ ሴቲንግ"
    reply_markup = ReplyKeyboardMarkup(keyboard,one_time_keyboard=True,resize_keyboard=True)
    update.message.reply_text(message, reply_markup=reply_markup)