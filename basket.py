from telegram.ext import *
from telegram import *
import DatabaseConnector as db
import menu as Menu
import restaurantSelection as rest
import Responses as res
import order as Order

count=[0]
food_holder=[]
food_price=[0]
resturant_name=[]

def basket(update,context,query=None):
    if query == None:
        telegramUserName = update['message']['chat']['first_name']
    else:
        telegramUserName = query['message']['chat']['first_name']
        food_price[0] = 0
        count[0] = 0

    username=telegramUserName.lower()+" basket"

    mycursor = db.mydb.cursor()
    mycursor.execute(f"SHOW TABLES LIKE '%{username}%'")
    myresult = mycursor.fetchall()

    if (len(myresult) > 0):

        mycursor = db.mydb.cursor()
        sql =f"SELECT COUNT(food) FROM `{username}`"
        mycursor.execute(sql)
        myResult=mycursor.fetchall()

        for x in myResult:
            count[0]=x[0]

        if count[0] > 0:
            mycursor = db.mydb.cursor()
            sql =f"Select * FROM `{username}`"
            mycursor.execute(sql)
            myResult=mycursor.fetchall()
            keyboard =[]

            for x in myResult:
                print(f"Food: {x[1]}")
                print(f"Food: {x[2]}")
                food_price[0] = food_price[0] + int(x[3])
                food_holder.append(x[1])
                food_holder.append(x[2])
                keyboard.append([InlineKeyboardButton(f"{x[1]} ❌", callback_data=f'foodid{x[0]}')],)

            keyboard.append([InlineKeyboardButton("Delete all food ❌", callback_data="delete")],)

            print(f"Food Holder: {food_holder}")

            if query == None:
                newline="\n"
                reply_markup = InlineKeyboardMarkup(keyboard)
                return update.message.reply_text(f"🧺 Basket:\n\n Resturant: {resturant_name[0].title()} \n\n{newline.join(str(x) for x in food_holder)}\n\nTotal Price: {food_price[0]} Birr",reply_markup=reply_markup)
            else:
                newline="\n"
                reply_markup = InlineKeyboardMarkup(keyboard)
                return query.edit_message_text(f"🧺 Basket:\n\n Resturant: {resturant_name[0].title()} \n\n{newline.join(str(x) for x in food_holder)}\n\nTotal Price: {food_price[0]} Birr",reply_markup=reply_markup)

        else:
            mycursor = db.mydb.cursor()
            sql = f"DROP TABLE `{username}`"
            mycursor.execute(sql)
            db.mydb.commit()

            i=0
            while(i<len(Menu.table_forMenu)):
                Menu.table_forMenu.pop()

            while(i<len(Order.total_food_to_be_ordered)):
                Order.total_food_to_be_ordered.pop()

            while(i<len(Order.overAllPrice)):
                Order.overAllPrice.pop()

            while(i<len(food_holder)):
                food_holder.pop()

            while(i<len(Order.food_to_be_added_to_database)):
                Order.food_to_be_added_to_database.pop()

            query.edit_message_text("Your Basket is empty lets fill it")
            rest.restaruntSelection(update, context, query)
    else:
        if query == None:
            update.message.reply_text("Your Basket is empty lets fill it")
            rest.restaruntSelection(update, context, query)
        else:
            query.edit_message_text("Your Basket is empty lets fill it")
            rest.restaruntSelection(update, context, query)


def basketAmharic(update,context,query=None):
    #print("You clicked basket")
    if query == None:
        telegramUserName=update['message']['chat']['first_name']
    else:
        telegramUserName=query['message']['chat']['first_name']
        food_price[0] = 0
        count[0] = 0

    username=telegramUserName.lower()+" basket"

    mycursor = db.mydb.cursor()
    mycursor.execute(f"SHOW TABLES LIKE '%{username}%'")
    myresult = mycursor.fetchall()

    if (len(myresult) > 0):

        mycursor = db.mydb.cursor()
        sql =f"SELECT COUNT(food) FROM `{username}`"
        mycursor.execute(sql)
        myResult=mycursor.fetchall()

        for x in myResult:
            count[0]=x[0]

        if count[0] > 0:
            mycursor = db.mydb.cursor()
            sql =f"Select * FROM `{username}`"
            mycursor.execute(sql)
            myResult=mycursor.fetchall()
            keyboard =[]

            for x in myResult:
                food_price[0] = food_price[0] + int(x[3])
                food_holder.append(x[1])
                food_holder.append(x[2])
                keyboard.append([
                    InlineKeyboardButton(f"{x[1]} ❌", callback_data=f'foodid{x[0]}')
                ],)

            keyboard.append([
                InlineKeyboardButton("ሁሉንም ምግብ ሰርዝ ❌", callback_data="delete")
            ],)

            print(f"Food Holder: {food_holder}")


            if query == None:
                newline="\n"
                reply_markup = InlineKeyboardMarkup(keyboard)
                return update.message.reply_text(f"🧺 ቅርጫት:\n\n ምግብ ቤት: {resturant_name[0].title()} \n\n{newline.join(str(x) for x in food_holder)}\n\nጠቅላላ ዋጋ: {food_price[0]} ብር",reply_markup=reply_markup)
            else:
                newline="\n"
                reply_markup = InlineKeyboardMarkup(keyboard)
                return query.edit_message_text(f"🧺 ቅርጫት:\n\n ምግብ ቤት: {resturant_name[0].title()} \n\n{newline.join(str(x) for x in food_holder)}\n\nጠቅላላ ዋጋ: {food_price[0]} ብር",reply_markup=reply_markup)

        else:
            mycursor = db.mydb.cursor()
            sql = f"DROP TABLE `{username}`"
            mycursor.execute(sql)
            db.mydb.commit()

            i=0
            while(i<len(Menu.table_forMenu)):
                Menu.table_forMenu.pop()

            while(i<len(Order.total_food_to_be_ordered)):
                Order.total_food_to_be_ordered.pop()

            while(i<len(Order.overAllPrice)):
                Order.overAllPrice.pop()

            while(i<len(food_holder)):
                food_holder.pop()

            while(i<len(Order.food_to_be_added_to_database)):
                Order.food_to_be_added_to_database.pop()

            query.edit_message_text("ቅርጫትዎ ባዶ ነው ይሙሉት።")
            rest.restaruntSelectionAmharic(update, context, query)

    else:
        if query == None:
            update.message.reply_text("ቅርጫትዎ ባዶ ነው ይሙሉት።")
            rest.restaruntSelectionAmharic(update, context, query)
        else:
            query.edit_message_text("ቅርጫትዎ ባዶ ነው ይሙሉት።")
            rest.restaruntSelectionAmharic(update, context, query)
