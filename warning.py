from telegram.ext import *
from telegram.ext.dispatcher import run_async
from telegram import *

def warning(update,context):
    #print("Warning")
    keyboard = [['I Agree', 'I Disagree']]
    message = "If you go back, all food in your basket will be lost because you can order food only from one restaurant at one time! Are you sure to go back?"
    reply_markup = ReplyKeyboardMarkup(keyboard,one_time_keyboard=True,resize_keyboard=True)
    update.message.reply_text(message, reply_markup=reply_markup)

def warningUpdated(update,context):
    #print("Warning")
    keyboard = [['Yes I Do', 'No I Don\'t']]
    message = "If you go back, all food in your basket will be lost because you can order food only from one restaurant at one time! Are you sure to go back?"
    reply_markup = ReplyKeyboardMarkup(keyboard,one_time_keyboard=True,resize_keyboard=True)
    update.message.reply_text(message, reply_markup=reply_markup)

def warningAmharic(update,context):
    #print("Warning")
    keyboard = [['አዎ እሳማማለሁ', 'አይ አልስማማም']]
    message = "ተመልሰው ከሄዱ በቅርጫትዎ ውስጥ ያለው ምግብ ሁሉ ይጠፋል ምክንያቱም አንድ ምግብ ቤት ውስጥ ብቻ ማዘዝ ስለሚችሉ። ይስማማሉ?"
    reply_markup = ReplyKeyboardMarkup(keyboard,one_time_keyboard=True,resize_keyboard=True)
    update.message.reply_text(message, reply_markup=reply_markup)


def warningAmharicUpdated(update,context):
    #print("Warning")
    keyboard = [['አዎ እፈልጋለሁ', 'አይ አልፈልግም']]
    message = "ተመልሰው ከሄዱ በቅርጫትዎ ውስጥ ያለው ምግብ ሁሉ ይጠፋል ምክንያቱም አንድ ምግብ ቤት ውስጥ ብቻ ማዘዝ ስለሚችሉ። ተመልሰው መሄድ ይፈልጋሉ ?"
    reply_markup = ReplyKeyboardMarkup(keyboard,one_time_keyboard=True,resize_keyboard=True)
    update.message.reply_text(message, reply_markup=reply_markup)