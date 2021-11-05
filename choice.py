from telegram.ext import *
from telegram import *
import Responses as R
import restaurantSelection as restaurant
import DatabaseConnector as db

def choice(update,context):
    keyboard = [['Choose Restaurant', '⚙️Setting']]
    message = "Let's order"
    reply_markup = ReplyKeyboardMarkup(keyboard,one_time_keyboard=True,resize_keyboard=True)
    update.message.reply_text(message, reply_markup=reply_markup)



def choiceAmharic(update,context):
    keyboard = [['ምግብ ቤት ይምረጡ', '⚙ ሴቲንግ']]
    message = "ምግብ እንዘዝ"
    reply_markup = ReplyKeyboardMarkup(keyboard,one_time_keyboard=True,resize_keyboard=True)
    update.message.reply_text(message, reply_markup=reply_markup)