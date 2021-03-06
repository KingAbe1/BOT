from telegram.ext import *
from telegram import *
import DatabaseConnector as db
import order as Order
import menu as Menu


def orderList(update,context):
    keyboard = [["๐งบ Basket", "๐ Order"],['Go Back','Restart the bot']]
    newline="\n"
    #message = f"Resturant: {Menu.table_forMenu[0]} \n\n{newline.join(str(x) for x in Order.total_food_to_be_ordered)}\n\nTotal Price: {Order.overAllPrice[0]} Birr"
    message = "Your food is ready if you wish to order it now please click the ๐ Order button you can also check your food order in ๐งบ Basket and if you don't feel like ordering food you can always go back by clicking Go Back button"
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
    update.message.reply_text(message, reply_markup=reply_markup)

def orderListAmharic(update,context):
    keyboard = [["๐งบ แแญแซแต", "๐ แแแ"],['แแฐ แแ แแต','แฆแฑแ แฅแแฐแแ แซแตแแแฉ']]
    newline="\n"
    #message = f"แแแฅ แคแต: {Menu.table_forMenu[0]} \n\n{newline.join(str(x) for x in Order.total_food_to_be_ordered)}\n\nแ แแแ แแ: {Order.overAllPrice[0]} แฅแญ"
    message = "แ แแ แแแแ แจแแแ แแแฅแ แแแ แแ แฅแฃแญแแ ๐ แแแ แแแแ แ แ แซแตแญแ แฅแแฒแแ แจแแแฅ แตแแแแแ ๐งบ แแญแซแต แแตแฅ แแแฐแฝ แญแฝแแ แฅแ แแแฅ แแแ แจแแญแแแ แจแแ แแฐ แแ แแต แแแแ แ แ แ แแตแจแ แแ แแ แฐแแแฐแ แแแต แญแฝแแแข"
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
    update.message.reply_text(message, reply_markup=reply_markup)