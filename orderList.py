from telegram.ext import *
from telegram import *
import DatabaseConnector as db
import order as Order
import menu as Menu


def orderList(update,context):
    keyboard = [["🧺 Basket", "🚚 Order"],['Go Back','Restart the bot']]
    newline="\n"
    #message = f"Resturant: {Menu.table_forMenu[0]} \n\n{newline.join(str(x) for x in Order.total_food_to_be_ordered)}\n\nTotal Price: {Order.overAllPrice[0]} Birr"
    message = "Your food is ready if you wish to order it now please click the 🚚 Order button you can also check your food order in 🧺 Basket and if you don't feel like ordering food you can always go back by clicking Go Back button"
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
    update.message.reply_text(message, reply_markup=reply_markup)

def orderListAmharic(update,context):
    keyboard = [["🧺 ቅርጫት", "🚚 ዕዘዝ"],['ወደ ኋላ ሂድ','ቦቱን እንደገና ያስጀምሩ']]
    newline="\n"
    #message = f"ምግብ ቤት: {Menu.table_forMenu[0]} \n\n{newline.join(str(x) for x in Order.total_food_to_be_ordered)}\n\nጠቅላላ ዋጋ: {Order.overAllPrice[0]} ብር"
    message = "አሁን ለማዘዝ ከፈለጉ ምግብዎ ዝግጁ ነው እባክዎን 🚚 ዕዘዝ ቁልፍን ጠቅ ያድርጉ እንዲሁም የምግብ ትዕዛዝዎን 🧺 ቅርጫት ውስጥ መፈተሽ ይችላሉ እና ምግብ ማዘዝ የማይፈልጉ ከሆነ ወደ ኋላ ሂድ ቁልፍን ጠቅ በማድረግ ሁል ጊዜ ተመልሰው መሄድ ይችላሉ።"
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
    update.message.reply_text(message, reply_markup=reply_markup)