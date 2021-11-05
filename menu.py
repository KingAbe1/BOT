from telegram.ext import *
from telegram.ext.dispatcher import run_async
from telegram import *
import DatabaseConnector as db
import basket as Basket
from math import *

table=[]
table_forMenu=[]



def menu(update,context,tableName):
    table_forMenu.append(tableName)
    table_name= tableName.lower()
    if len(table)==0:
        table.append(table_name)
        Basket.resturant_name.append(tableName)
    else:
        table.pop()
        Basket.resturant_name.pop()
        table.append(table_name)
        Basket.resturant_name.append(tableName)

    mycursor = db.mydb.cursor()
    mycursor.execute(f"SELECT Name1 FROM items WHERE Restaurant = '{table_name}'")
    myresult = mycursor.fetchall()

    count = ceil(len(myresult) / 2)
    row = 0
    keyboard =[[]]

    for y in myresult:
        if row != (count):
            if len(keyboard[row]) <= 1:
                print(f"Row: {row}")
                keyboard[row].append(f"{y[0]}")
            else:
                keyboard.append([])
                row = row + 1
                keyboard[row].append(f"{y[0]}")


    keyboard.append(["back","Restart the bot"])
    message = f"{tableName} \n\nPlease select food from menu 👇 below."
    reply_markup = ReplyKeyboardMarkup(keyboard,one_time_keyboard=True,resize_keyboard=True)
    update.message.reply_text(message, reply_markup=reply_markup)

def menuAmharic(update,context,tableName):
    table_forMenu.append(tableName)
    table_name= tableName.lower()
    if len(table)==0:
        table.append(table_name)
        Basket.resturant_name.append(tableName)
    else:
        table.pop()
        Basket.resturant_name.pop()
        table.append(table_name)
        Basket.resturant_name.append(tableName)

    mycursor = db.mydb.cursor()
    mycursor.execute(f"SELECT Name2 FROM items WHERE Restaurant = '{table_name}'")
    myresult = mycursor.fetchall()

    count = ceil(len(myresult) / 2)
    row = 0
    keyboard =[[]]

    for y in myresult:
        if row != (count):
            if len(keyboard[row]) <= 1:
                print(f"Row: {row}")
                keyboard[row].append(f"{y[0]}")
            else:
                keyboard.append([])
                row = row + 1
                keyboard[row].append(f"{y[0]}")

    keyboard.append(["ወደ ኋላ ተመለስ","ቦቱን እንደገና ያስጀምሩ"])
    message = f"{tableName} \n\nእባክዎን ከዚህ በታች 👇 ካለው ምግብ ይምረጡ።"
    reply_markup = ReplyKeyboardMarkup(keyboard,one_time_keyboard=True,resize_keyboard=True)
    update.message.reply_text(message, reply_markup=reply_markup)