from telegram import *
from telebot import *
from telegram.ext import *
from telegram.ext.dispatcher import run_async
import Constant as Keys
import Responses as R
import contact as Contact
import lang as Language
import menu as Menu
import restaurantSelection as Restaurant
import DatabaseConnector as db
import order as Order
import numberOfFood as NumberOfFood
import orderList as OrderList
import warning as Warning
import basket as Basket
import choice as Choice
import location as Location
import setting as Setting
import confirmation as Confirmation

print("Bot started...")

def start_command(update,context):
    telegramUserName=update['message']['chat']['first_name']
    username=telegramUserName.lower()+" basket"
    mycursor = db.mydb.cursor()
    mycursor.execute(f"SHOW TABLES LIKE '%{username}%'")
    myresult = mycursor.fetchall()

    if (len(myresult) > 0):
        mycursor = db.mydb.cursor()
        sql = f"DROP TABLE `{username}`"
        mycursor.execute(sql)
        db.mydb.commit()

        i=0
        if len(Order.food_to_be_added_to_database) >0:
            while(i < len(Order.food_to_be_added_to_database)):
                Order.food_to_be_added_to_database.pop()

        if len(Menu.table_forMenu) >0:
            while(i<len(Menu.table_forMenu)):
                Menu.table_forMenu.pop()

        if len(Order.total_food_to_be_ordered) >0:
            while(i<len(Order.total_food_to_be_ordered)):
                Order.total_food_to_be_ordered.pop()

        if len(Order.overAllPrice) >0:
            while(i<len(Order.overAllPrice)):
                Order.overAllPrice.pop()

        if len(Basket.food_holder) >0:
            while(i<len(Basket.food_holder)):
                Basket.food_holder.pop()
        print("inside the main function")
        if len(Location.food_holder) >0:
            while(i<len(Location.food_holder)):
                Location.food_holder.pop()

        if len(Confirmation.item) >0:
            while(i<len(Confirmation.item)):
                Confirmation.item.pop()

        if len(R.tableName) >0:
            R.tableName.pop()

    mycursor = db.mydb.cursor()
    sql =f"Select language FROM clients where userName='{telegramUserName}'"
    mycursor.execute(sql)
    myResult=mycursor.fetchall()

    if len(myResult) > 0:

        for x in myResult:
            if x[0] == "English":
                Choice.choice(update,context)
            elif x[0] == "Amharic":
                Choice.choiceAmharic(update, context)
    else:
        update.message.reply_text(f"😉 Hello, {telegramUserName}!")
        Language.language(update,context)



def handle_message(update,context):
    randomString=str(update.message.text)
    R.sample_responses(randomString,update, context)


def help_command(update,context):
    update.message.reply_text("if you need help you should contact @fere012")


def button_clicked(update,context):
    query = update.callback_query
    query.answer()
    if (query.data).startswith("foodid"):
        # print("foodid")
        telegramUserName=query['message']['chat']['first_name']
        username=telegramUserName.lower()+" basket"

        mycursor = db.mydb.cursor()
        sql =f"Select language FROM clients where userName='{telegramUserName}'"
        mycursor.execute(sql)
        myResult=mycursor.fetchall()

        if len(myResult) > 0:
            for x in myResult:
                if x[0] == "English":
                    mycursor = db.mydb.cursor()
                    mycursor.execute(f"SELECT * FROM `{username}`")
                    myresult = mycursor.fetchall()

                    for x in myresult:
                        if query.data == f"foodid{x[0]}":
                            mycursor = db.mydb.cursor()
                            mycursor.execute(f"DELETE FROM `{username}` WHERE food = '{x[1]}'")
                            db.mydb.commit()

                    i=0
                    while(i<len(Basket.food_holder)):
                        Basket.food_holder.pop()

                    Basket.basket(update, context, query)
                else:
                    mycursor = db.mydb.cursor()
                    mycursor.execute(f"SELECT * FROM `{username}`")
                    myresult = mycursor.fetchall()

                    for x in myresult:
                        if query.data == f"foodid{x[0]}":
                            mycursor = db.mydb.cursor()
                            mycursor.execute(f"DELETE FROM `{username}` WHERE food = '{x[1]}'")
                            db.mydb.commit()

                    i=0
                    while(i<len(Basket.food_holder)):
                        Basket.food_holder.pop()

                    Basket.basketAmharic(update, context, query)

    elif query.data  == "delete":
        print("DELETE ALL")
        telegramUserName=query['message']['chat']['first_name']
        username=telegramUserName.lower()+" basket"

        mycursor = db.mydb.cursor()
        sql =f"Select language FROM clients where userName='{telegramUserName}'"
        mycursor.execute(sql)
        myResult=mycursor.fetchall()

        for x in myResult:
            if x[0] == "English":
                mycursor = db.mydb.cursor()
                sql = f"DELETE FROM `{username}`"
                mycursor.execute(sql)
                db.mydb.commit()
                Basket.basket(update, context, query)
            else:
                mycursor = db.mydb.cursor()
                sql = f"DELETE FROM `{username}`"
                mycursor.execute(sql)
                db.mydb.commit()
                Basket.basketAmharic(update, context, query)


def error(update,context):
    print(f"{update}\n{update['message']['text']} caused error {context.error}")

def status(update,context):
    telegramUserName = update['message']['chat']['first_name']
    mycursor = db.mydb.cursor()
    mycursor.execute(f"SELECT id FROM clients WHERE userName='{telegramUserName}'")
    result = mycursor.fetchall()
    for x in result:
        ID = x[0]

    mycursor = db.mydb.cursor()
    mycursor.execute(f"SELECT Status FROM orders WHERE Customer_Id = '{ID}'")
    result = mycursor.fetchall()
    for x in result:
        print(f"Value: {x[0]}")
        if x[0] == "Accepted":
            update.message.reply_text(text="👍 Your order have been Accepted.\nThank you for ordering using our telegram bot.")

            mycursor = db.mydb.cursor()
            sql =f"Select language FROM clients where userName='{telegramUserName}'"
            mycursor.execute(sql)
            checker = mycursor.fetchall()
            for x in checker:
                if x[0] == "English":
                    Choice.choice(update,context)
                else:
                    Choice.choiceAmharic(update, context)
            break

        elif x[0] == "Pending":
            update.message.reply_text(text="Our guys in the call center will call you to confirm your order.")
            break

    mycursor = db.mydb.cursor()
    mycursor.execute(f"SELECT COUNT(Status) FROM orders WHERE Customer_Id = '{ID}'")
    result = mycursor.fetchall()
    for x in result:
        if x[0] == 0:
            update.message.reply_text(text="Your order have been canceled.")

            mycursor = db.mydb.cursor()
            sql =f"Select language FROM clients where userName='{telegramUserName}'"
            mycursor.execute(sql)
            checker = mycursor.fetchall()
            for x in checker:
                if x[0] == "English":
                    Choice.choice(update,context)
                else:
                    Choice.choiceAmharic(update, context)

            break


def basket(update,context):
    telegramUserName=update['message']['chat']['first_name']
    username=telegramUserName.lower()+" basket"

    mycursor = db.mydb.cursor()
    sql =f"Select language FROM clients where userName='{telegramUserName}'"
    mycursor.execute(sql)
    checker = mycursor.fetchall()
    for x in checker:
        if x[0] == "English":
            Basket.basket(update,context)
        else:
           Basket.basketAmharic(update, context)

def setting(update,context):
    telegramUserName=update['message']['chat']['first_name']
    username=telegramUserName.lower()+" basket"

    mycursor = db.mydb.cursor()
    sql =f"Select language FROM clients where userName='{telegramUserName}'"
    mycursor.execute(sql)
    checker = mycursor.fetchall()
    for x in checker:
        if x[0] == "English":
            Setting.setting(update, context)
            R.personalInfo.pop()
        else:
            Setting.settingAmharic(update, context)
            R.personalInfo.pop()


def restaurant(update,context):
    telegramUserName=update['message']['chat']['first_name']
    username=telegramUserName.lower()+" basket"

    mycursor = db.mydb.cursor()
    sql =f"Select language FROM clients where userName='{telegramUserName}'"
    mycursor.execute(sql)
    checker = mycursor.fetchall()
    for x in checker:
        if x[0] == "English":
            Restaurant.restaruntSelection(update, context)
            R.personalInfo.pop()
        else:
            Restaurant.restaruntSelectionAmharic(update, context)
            R.personalInfo.pop()

def main():
    updater = Updater(Keys.API_KEY,use_context=True,workers=100)
    dp=updater.dispatcher

    dp.add_handler(CommandHandler("start",start_command,run_async=True))
    dp.add_handler(CommandHandler("help",help_command,run_async=True))
    dp.add_handler(CommandHandler("restaurant",restaurant,run_async=True))
    dp.add_handler(CommandHandler("setting",setting,run_async=True))
    dp.add_handler(CommandHandler("basket",basket,run_async=True))
    dp.add_handler(CommandHandler("status",status,run_async=True))
    dp.add_handler(MessageHandler(Filters.text,handle_message,run_async=True))
    dp.add_handler(CallbackQueryHandler(button_clicked,run_async=True))
    dp.add_handler(MessageHandler(Filters.contact,Contact.contact_callback,run_async=True))
    dp.add_handler(MessageHandler(Filters.location,Location.location,run_async=True))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()