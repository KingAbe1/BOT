from telegram.ext import *
from telegram.ext.dispatcher import run_async
from telegram import *
import DatabaseConnector as db
from math import *


def restaruntSelection(update,context, query = None):
    if query == None:
        telegramUserName = update['message']['chat']['first_name']
    else:
        telegramUserName = query['message']['chat']['first_name']


    mycursor = db.mydb.cursor()
    sql =f"Select fullName FROM clients where userName='{telegramUserName}'"
    mycursor.execute(sql)
    myResult=mycursor.fetchall()
    for x in myResult:
        updateResult=x[0]

    mycursor = db.mydb.cursor()
    mycursor.execute("SELECT Name1 FROM restaurants")
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


    keyboard.append(["Back"])
    message = f"Welcome {updateResult} \n\nPlease select restaurant from 👇 below."
    reply_markup = ReplyKeyboardMarkup(keyboard,one_time_keyboard=True,resize_keyboard=True)

    if query == None:
        update.message.reply_text(message, reply_markup=reply_markup)
    else:
        query.message.reply_text(message, reply_markup=reply_markup)


def restaruntSelectionAmharic(update,context, query = None):

    if query == None:
        telegramUserName = update['message']['chat']['first_name']
    else:
        telegramUserName = query['message']['chat']['first_name']

    #print(telegramUserName)

    mycursor = db.mydb.cursor()
    sql =f"Select fullName FROM clients where userName='{telegramUserName}'"

    mycursor.execute(sql)
    myResult=mycursor.fetchall()
    for x in myResult:
        updateResult=x[0]

    mycursor = db.mydb.cursor()
    mycursor.execute("SELECT Name2 FROM restaurants")
    myresult = mycursor.fetchall()

    count = ceil(len(myresult) / 2)
    row = 0
    keyboard =[[]]

    for y in myresult:
        if row != (count):
            if len(keyboard[row]) <= 1:
                keyboard[row].append(f"{y[0]}")
            else:
                keyboard.append([])
                row = row + 1
                keyboard[row].append(f"{y[0]}")

    keyboard.append(["ተመለስ"])
    #print("Passed it")
    message = f"እንኳን በደህና መጡ {updateResult} \n\nእባክዎን ከታች 👇 ካለው አንድ ምግብ ቤት ይምረጡ።"
    reply_markup = ReplyKeyboardMarkup(keyboard,one_time_keyboard=True,resize_keyboard=True)
    if query == None:
        #print("Query none type")
        update.message.reply_text(message, reply_markup=reply_markup)
    else:
        query.message.reply_text(message, reply_markup=reply_markup)