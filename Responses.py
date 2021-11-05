from telegram.ext import *
from telegram import *
import contact as Contact
import DatabaseConnector as db
import Constant as Keys
import time
import restaurantSelection as Restaurant
import setting as Setting
import choice as Choice
import order as Order
import menu as Menu
import numberOfFood as NumberOfFood
import orderList as OrderList
import warning as Warning
import basket as Basket
import location as Location
import confirmation as Confirmation


menuName=[""]
personalInfo=[]
tableName=[]
resCount=[""]
menCount=[0]
count=0
newName=[]


def sample_responses(randomString,update,context):
    telegramUserName = update['message']['chat']['first_name']
    mycursor = db.mydb.cursor()
    sql =f"Select language FROM clients where userName='{telegramUserName}'"
    mycursor.execute(sql)
    checker = mycursor.fetchall()

    personalInfo.append(randomString)

    if randomString.__eq__("Change Name") or randomString.__eq__("ስም ቀይር"):
        newName.append(randomString)

    try:
        if randomString.isnumeric() == False:
            for x in checker:
                if x[0] == "English":
                    if randomString != "back":
                        if len(tableName) > 0:
                            mycursor = db.mydb.cursor()
                            print(f"Table name: {tableName[0]}")
                            mycursor.execute(f"SELECT COUNT(Name1) FROM restaurants WHERE Name1 = '{tableName[0]}'")
                            myresult = mycursor.fetchall()
                            for x in myresult:
                                resCount[0] = x[0]

                            if randomString != "I Disagree":
                                if randomString != "I Agree":
                                    if randomString != "yes":
                                        if randomString != "no":
                                            print(f"resCount: {resCount[0]}")
                                            if resCount[0] > 0:
                                                personalInfo.pop()
                                                Order.order(update,context,f"{randomString}")
                        else:
                            mycursor = db.mydb.cursor()
                            mycursor.execute(f"SELECT COUNT(Name1) FROM restaurants WHERE Name1='{randomString}'")
                            myresult = mycursor.fetchall()
                            for x in myresult:
                                resCount[0]=x[0]
                            if resCount[0] > 0:
                                tableName.append(randomString)
                                Menu.menu(update,context,tableName[0])
                                personalInfo.pop()
                else:
                    if randomString != "ወደ ኋላ ተመለስ":
                        if len(tableName) > 0:
                            mycursor = db.mydb.cursor()
                            mycursor.execute(f"SELECT COUNT(Name2) FROM restaurants WHERE Name1 = '{tableName[0]}'")
                            myresult = mycursor.fetchall()
                            for x in myresult:
                                resCount[0] = x[0]

                            if randomString != "አይ አልስማማም":
                                if randomString != "አዎ እሳማማለሁ":
                                    if randomString != "አዎ":
                                        if randomString != "አይ":
                                            if resCount[0] > 0:
                                                personalInfo.pop()
                                                Order.orderAmharic(update,context,f"{randomString}")
                        else:
                            mycursor = db.mydb.cursor()
                            mycursor.execute(f"SELECT COUNT(Name2) FROM restaurants WHERE Name2='{randomString}'")
                            myresult = mycursor.fetchall()
                            for x in myresult:
                                resCount[0]=x[0]
                            if resCount[0] > 0:
                                mycursor = db.mydb.cursor()
                                mycursor.execute(f"SELECT Name1 FROM restaurants WHERE Name2='{randomString}'")
                                resName = mycursor.fetchall()
                                for x in resName:
                                    tableName.append(x[0])
                                    Menu.menuAmharic(update,context,tableName[0])
                                    personalInfo.pop()

    except:
        print("Integer")

    if randomString.__eq__("English"):
        update.message.reply_text(text="Your language has been set to English")
        update.message.reply_text(text="Enter your Full Name")

    elif randomString.__eq__("Choose Restaurant"):
        Restaurant.restaruntSelection(update,context)
        personalInfo.pop()

    elif randomString.__eq__("ምግብ ቤት ይምረጡ"):
        Restaurant.restaruntSelectionAmharic(update, context)
        personalInfo.pop()

    elif randomString.__eq__("Restart the bot"):
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

            if len(Location.food_holder) >0:
                while(i<len(Location.food_holder)):
                    Location.food_holder.pop()

            if len(Confirmation.item) >0:
                while(i<len(Confirmation.item)):
                    Confirmation.item.pop()

            if len(tableName) >0:
                tableName.pop()

            Choice.choice(update, context)
            personalInfo.pop()

    elif randomString.__eq__("ቦቱን እንደገና ያስጀምሩ"):
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

            if len(Location.food_holder) >0:
                while(i<len(Location.food_holder)):
                    Location.food_holder.pop()

            if len(Confirmation.item) >0:
                while(i<len(Confirmation.item)):
                    Confirmation.item.pop()

            if len(tableName) >0:
                tableName.pop()

            Choice.choiceAmharic(update, context)

    elif randomString.__eq__("Back"):
        Choice.choice(update, context)
        personalInfo.pop()

    elif randomString.__eq__("ተመለስ"):
        Choice.choiceAmharic(update, context)
        personalInfo.pop()

    elif randomString.__eq__("I Agree"):
        telegramUserName=update['message']['chat']['first_name']
        username=telegramUserName.lower()+" basket"

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

        while(i<len(Basket.food_holder)):
            Basket.food_holder.pop()

        while(i<len(Order.food_to_be_added_to_database)):
            Order.food_to_be_added_to_database.pop()

        Restaurant.restaruntSelection(update, context)
        tableName.pop()

    elif randomString.__eq__("Yes I Do"):
        telegramUserName=update['message']['chat']['first_name']
        username=telegramUserName.lower()+" basket"

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

        while(i<len(Basket.food_holder)):
            Basket.food_holder.pop()

        while(i<len(Order.food_to_be_added_to_database)):
            Order.food_to_be_added_to_database.pop()

        Restaurant.restaruntSelection(update, context)

        if len(tableName) > 0:
            tableName.pop()

    elif randomString.__eq__("አዎ እሳማማለሁ" ):
        telegramUserName=update['message']['chat']['first_name']
        username=telegramUserName.lower()+" basket"

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

        while(i<len(Basket.food_holder)):
            Basket.food_holder.pop()

        while(i<len(Order.food_to_be_added_to_database)):
            Order.food_to_be_added_to_database.pop()

        Restaurant.restaruntSelectionAmharic(update, context)

        if len(tableName) > 0:
            tableName.pop()

    elif randomString.__eq__("አዎ እፈልጋለሁ"):
        telegramUserName=update['message']['chat']['first_name']
        username=telegramUserName.lower()+" basket"

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

        while(i<len(Basket.food_holder)):
            Basket.food_holder.pop()

        while(i<len(Order.food_to_be_added_to_database)):
            Order.food_to_be_added_to_database.pop()

        Restaurant.restaruntSelectionAmharic(update, context)

        if len(tableName) > 0:
            tableName.pop()


    elif randomString.__eq__("I Disagree"):
        print("I disagree")
        i=0
        while(i<len(Order.food_to_be_added_to_database)):
            Order.food_to_be_added_to_database.pop()

        table_name_from_menu = Menu.table[0]
        tableName.append(table_name_from_menu.title())
        Menu.menu(update,context,tableName[0])

        if len(Basket.food_holder) > 0:
            while(i<len(Basket.food_holder)):
                Basket.food_holder.pop()

    elif randomString.__eq__("No I Don\'t"):
        print("I disagree")
        i=0
        while(i<len(Order.food_to_be_added_to_database)):
            Order.food_to_be_added_to_database.pop()

        print("Before order List")
        OrderList.orderList(update, context)

        if len(Basket.food_holder) > 0:
            while(i<len(Basket.food_holder)):
                Basket.food_holder.pop()

    elif randomString.__eq__("አይ አልስማማም"):
        i=0
        while(i<len(Order.food_to_be_added_to_database)):
            Order.food_to_be_added_to_database.pop()

        table_name_from_menu = Menu.table[0]
        tableName.append(table_name_from_menu.title())
        Menu.menuAmharic(update,context,tableName[0])

        if len(Basket.food_holder) > 0:
            while(i<len(Basket.food_holder)):
                Basket.food_holder.pop()

    elif randomString.__eq__("አይ አልፈልግም"):
        i=0
        while(i<len(Order.food_to_be_added_to_database)):
            Order.food_to_be_added_to_database.pop()

        print("Not here")
        OrderList.orderListAmharic(update, context)

        if len(Basket.food_holder) > 0:
            while(i<len(Basket.food_holder)):
                Basket.food_holder.pop()


    elif randomString.__eq__("Change language to Amharic"):
        telegramUserName=update['message']['chat']['first_name']
        mycursor = db.mydb.cursor()
        sql = "UPDATE clients SET language = 'Amharic' WHERE language = 'English'"
        mycursor.execute(sql)
        db.mydb.commit()
        Setting.settingAmharic(update, context)

    elif randomString.__eq__("ቋንቋውን ወደ እንግሊዝኛ ይለውጡ"):
        telegramUserName=update['message']['chat']['first_name']
        mycursor = db.mydb.cursor()
        sql = "UPDATE clients SET language = 'English' WHERE language = 'Amharic'"
        mycursor.execute(sql)
        db.mydb.commit()
        Setting.setting(update, context)

    elif randomString.__eq__("Change Name"):

        update.message.reply_text("Please write your full name")

    elif randomString.__eq__("ስም ቀይር"):

        update.message.reply_text("እባክዎን ሙሉ ስምዎን ይፃፉ")

    elif len(newName) > 0:
        telegramUserName=update['message']['chat']['first_name']
        mycursor = db.mydb.cursor()
        sql = f"UPDATE clients SET fullName = '{randomString}' WHERE userName = '{telegramUserName}'"
        mycursor.execute(sql)
        db.mydb.commit()

        mycursor = db.mydb.cursor()
        sql =f"Select language FROM clients where userName='{telegramUserName}'"
        mycursor.execute(sql)
        myResult=mycursor.fetchall()

        if len(myResult) > 0:
            for x in myResult:
                if x[0] == "English":
                    update.message.reply_text(f"Your name has changed to {randomString}")
                    Setting.setting(update, context)
                elif x[0] == "Amharic":
                    update.message.reply_text(f"ስምህ ወደ {randomString} ተለውጧል።")
                    Setting.settingAmharic(update, context)
            newName.pop()

    elif randomString.__eq__("back"):
        telegramUserName=update['message']['chat']['first_name']
        username=telegramUserName.lower()+" basket"

        mycursor = db.mydb.cursor()
        mycursor.execute(f"SHOW TABLES LIKE '%{username}%'")
        myresult = mycursor.fetchall()

        if len(myresult) > 0:
            Warning.warning(update,context)
        else:
            Restaurant.restaruntSelection(update,context)
            tableName.pop()

    elif randomString.__eq__("Go Back"):
        telegramUserName=update['message']['chat']['first_name']
        username=telegramUserName.lower()+" basket"

        mycursor = db.mydb.cursor()
        mycursor.execute(f"SHOW TABLES LIKE '%{username}%'")
        myresult = mycursor.fetchall()

        if len(myresult) > 0:
            Warning.warningUpdated(update,context)
        else:
            Restaurant.restaruntSelection(update,context)
            tableName.pop()

    elif randomString.__eq__("ወደ ኋላ ተመለስ"):
        telegramUserName=update['message']['chat']['first_name']
        username=telegramUserName.lower()+" basket"

        mycursor = db.mydb.cursor()
        mycursor.execute(f"SHOW TABLES LIKE '%{username}%'")
        myresult = mycursor.fetchall()

        if len(myresult) > 0:
            Warning.warningAmharic(update,context)
        else:
            Restaurant.restaruntSelectionAmharic(update,context)
            tableName.pop()

    elif randomString.__eq__("ወደ ኋላ ሂድ"):
        print("ወደ ኋላ ተመለስ")
        telegramUserName=update['message']['chat']['first_name']
        username=telegramUserName.lower()+" basket"

        mycursor = db.mydb.cursor()
        mycursor.execute(f"SHOW TABLES LIKE '%{username}%'")
        myresult = mycursor.fetchall()

        if len(myresult) > 0:
            Warning.warningAmharicUpdated(update,context)
        else:
            Restaurant.restaruntSelectionAmharic(update,context)
            tableName.pop()

    elif randomString.__eq__("⚙️Setting"):
        Setting.setting(update, context)
        personalInfo.pop()

    elif randomString.__eq__("⚙ ሴቲንግ"):
        Setting.settingAmharic(update, context)
        personalInfo.pop()

    elif randomString.__eq__("yes"):
        i=0
        while(i<len(Order.food_to_be_added_to_database)):
            Order.food_to_be_added_to_database.pop()
        Menu.menu(update, context,f"{tableName[0].lower()}")
        personalInfo.pop()

    elif randomString.__eq__("አዎ"):
        i=0
        while(i<len(Order.food_to_be_added_to_database)):
            Order.food_to_be_added_to_database.pop()
        Menu.menuAmharic(update, context,f"{tableName[0].lower()}")
        personalInfo.pop()


    elif randomString.__eq__("no"):
        if len(personalInfo) > 0:
            personalInfo.pop()

        OrderList.orderList(update, context)

        tableName.pop()

    elif randomString.__eq__("አይ"):
        if len(personalInfo) > 0:
            personalInfo.pop()

        OrderList.orderListAmharic(update, context)

        tableName.pop()


    elif randomString.__eq__("🧺 Basket"):
        Basket.basket(update,context)

    elif randomString.__eq__("🧺 ቅርጫት"):
        Basket.basketAmharic(update,context)

    elif randomString.__eq__("🚚 Order"):
        Location.location(update, context)

        i=0
        while(i<len(Order.total_food_to_be_ordered)):
            Order.total_food_to_be_ordered.pop()

        while(i<len(Order.overAllPrice)):
            Order.overAllPrice.pop()

        while(i<len(Menu.table_forMenu)):
            Menu.table_forMenu.pop()

        if len(tableName) >0:
            tableName.pop()

    elif randomString.__eq__("🚚 ዕዘዝ"):
        Location.location(update, context)

        i=0
        while(i<len(Order.total_food_to_be_ordered)):
            Order.total_food_to_be_ordered.pop()

        while(i<len(Order.overAllPrice)):
            Order.overAllPrice.pop()

        while(i<len(Menu.table_forMenu)):
            Menu.table_forMenu.pop()

        if len(tableName) > 0:
            tableName.pop()

    elif randomString.__eq__("🚖 Order it"):
        Confirmation.tableRes.append(Basket.resturant_name[0].title())
        Confirmation.confirmation(update, context)

    elif randomString.__eq__("🚖 ይዘዙት"):
        Confirmation.tableRes.append(Basket.resturant_name[0].title())
        Confirmation.confirmationAmharic(update, context)

    elif randomString.__eq__("🙀 Maybe later"):

        i = 0
        while(i < len(Order.food_to_be_added_to_database)):
            Order.food_to_be_added_to_database.pop()

        while(i<len(Menu.table_forMenu)):
            Menu.table_forMenu.pop()

        while(i<len(Order.total_food_to_be_ordered)):
            Order.total_food_to_be_ordered.pop()

        while(i<len(Order.overAllPrice)):
            Order.overAllPrice.pop()

        while(i<len(Basket.food_holder)):
            Basket.food_holder.pop()

        while(i<len(Location.food_holder)):
            Location.food_holder.pop()

        while(i<len(Order.food_to_be_added_to_database)):
            Order.food_to_be_added_to_database.pop()

        # tableName.pop()

        telegramUserName=update['message']['chat']['first_name']
        username=telegramUserName.lower()+" basket"

        mycursor = db.mydb.cursor()
        sql = f"DROP TABLE `{username}`"
        mycursor.execute(sql)
        db.mydb.commit()
        Restaurant.restaruntSelection(update, context)

    elif randomString.__eq__("🙀 ምናልባት በኋላ"):

        i = 0

        while(i < len(Order.food_to_be_added_to_database)):
            Order.food_to_be_added_to_database.pop()

        while(i<len(Menu.table_forMenu)):
            Menu.table_forMenu.pop()

        while(i<len(Order.total_food_to_be_ordered)):
            Order.total_food_to_be_ordered.pop()

        while(i<len(Order.overAllPrice)):
            Order.overAllPrice.pop()

        while(i<len(Basket.food_holder)):
            Basket.food_holder.pop()

        while(i<len(Location.food_holder)):
            Location.food_holder.pop()

        while(i<len(Order.food_to_be_added_to_database)):
            Order.food_to_be_added_to_database.pop()

        # tableName.pop()

        telegramUserName=update['message']['chat']['first_name']
        username=telegramUserName.lower()+" basket"

        mycursor = db.mydb.cursor()
        sql = f"DROP TABLE `{username}`"
        mycursor.execute(sql)
        db.mydb.commit()
        Restaurant.restaruntSelectionAmharic(update, context)


    elif "1" in update.message.text:
        telegramUserName = update['message']['chat']['first_name']
        username = telegramUserName.lower()+" basket"
        for x in checker:
            if x[0] == "English":
                mycursor = db.mydb.cursor()
                mycursor.execute(f"SELECT Price FROM items WHERE Restaurant = '{Order.calculatePrice[1]}' AND Name1 = '{Order.calculatePrice[0]}'")
                myresult = mycursor.fetchall()
                for x in myresult:
                    price = 1 * x[0]
                    Order.totalPrice(update, context, price)
                    Order.total_food_to_be_ordered.append(f"1 x {x[0]} = {price} Birr")

                sql = f"UPDATE `{username}` SET calculatePrice = '1 x {x[0]} = {price} Birr' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

                sql = f"UPDATE `{username}` SET price = '{price}' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

            else:
                mycursor = db.mydb.cursor()
                mycursor.execute(f"SELECT Price FROM items WHERE Restaurant = '{Order.calculatePrice[1]}' AND Name2 = '{Order.calculatePrice[0]}'")
                myresult = mycursor.fetchall()
                for x in myresult:
                    price = 1 * x[0]
                    Order.totalPrice(update, context, price)
                    Order.total_food_to_be_ordered.append(f"1 x {x[0]} = {price} ብር")

                sql = f"UPDATE `{username}` SET calculatePrice = '1 x {x[0]} = {price} ብር' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

                sql = f"UPDATE `{username}` SET price = '{price}' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

        for x in checker:
            if x[0] == "English":
                NumberOfFood.numberoffood(update, context)
            else:
                NumberOfFood.numberoffoodAmharic(update, context)

    elif "2" in update.message.text:
        telegramUserName=update['message']['chat']['first_name']
        username=telegramUserName.lower()+" basket"
        for x in checker:
            if x[0] == "English":
                mycursor = db.mydb.cursor()
                mycursor.execute(f"SELECT Price FROM items WHERE Restaurant = '{Order.calculatePrice[1]}' AND Name1 = '{Order.calculatePrice[0]}'")
                myresult = mycursor.fetchall()
                for x in myresult:
                    price=2 * x[0]
                    Order.totalPrice(update, context,price)
                    Order.total_food_to_be_ordered.append(f"2 x {x[0]} = {price} Birr")

                sql = f"UPDATE `{username}` SET calculatePrice = '2 x {x[0]} = {price} Birr' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

                sql = f"UPDATE `{username}` SET price = '{price}' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

            else:
                mycursor = db.mydb.cursor()
                mycursor.execute(f"SELECT Price FROM items WHERE Restaurant = '{Order.calculatePrice[1]}' AND Name2 = '{Order.calculatePrice[0]}'")
                myresult = mycursor.fetchall()
                for x in myresult:
                    price=2 * x[0]
                    Order.totalPrice(update, context,price)
                    Order.total_food_to_be_ordered.append(f"2 x {x[0]} = {price} ብር")

                sql = f"UPDATE `{username}` SET calculatePrice = '2 x {x[0]} = {price} ብር' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

                sql = f"UPDATE `{username}` SET price = '{price}' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

        for x in checker:
            if x[0] == "English":
                NumberOfFood.numberoffood(update, context)
            else:
                NumberOfFood.numberoffoodAmharic(update, context)

    elif "3" in update.message.text:
        telegramUserName=update['message']['chat']['first_name']
        username=telegramUserName.lower()+" basket"
        for x in checker:
            if x[0] == "English":
                mycursor = db.mydb.cursor()
                mycursor.execute(f"SELECT Price FROM items WHERE Restaurant = '{Order.calculatePrice[1]}' AND Name1 = '{Order.calculatePrice[0]}'")
                myresult = mycursor.fetchall()
                for x in myresult:
                    price=3 * x[0]
                    Order.totalPrice(update, context,price)
                    Order.total_food_to_be_ordered.append(f"3 x {x[0]} = {price} Birr")

                sql = f"UPDATE `{username}` SET calculatePrice = '3 x {x[0]} = {price} Birr' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

                sql = f"UPDATE `{username}` SET price = '{price}' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

            else:
                mycursor = db.mydb.cursor()
                mycursor.execute(f"SELECT Price FROM items WHERE Restaurant = '{Order.calculatePrice[1]}' AND Name2 = '{Order.calculatePrice[0]}'")
                myresult = mycursor.fetchall()
                for x in myresult:
                    price=3 * x[0]
                    Order.totalPrice(update, context,price)
                    Order.total_food_to_be_ordered.append(f"3 x {x[0]} = {price} ብር")

                sql = f"UPDATE `{username}` SET calculatePrice = '3 x {x[0]} = {price} ብር' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

                sql = f"UPDATE `{username}` SET price = '{price}' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

        for x in checker:
            if x[0] == "English":
                NumberOfFood.numberoffood(update, context)
            else:
                NumberOfFood.numberoffoodAmharic(update, context)

    elif "4" in update.message.text:
        telegramUserName=update['message']['chat']['first_name']
        username=telegramUserName.lower()+" basket"
        for x in checker:
            if x[0] == "English":
                mycursor = db.mydb.cursor()
                mycursor.execute(f"SELECT Price FROM items WHERE Restaurant = '{Order.calculatePrice[1]}' AND Name1 = '{Order.calculatePrice[0]}'")
                myresult = mycursor.fetchall()
                for x in myresult:
                    price=4 * x[0]
                    Order.totalPrice(update, context,price)
                    Order.total_food_to_be_ordered.append(f"4 x {x[0]} = {price} Birr")

                sql = f"UPDATE `{username}` SET calculatePrice = '4 x {x[0]} = {price} Birr' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

                sql = f"UPDATE `{username}` SET price = '{price}' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

            else:
                mycursor = db.mydb.cursor()
                mycursor.execute(f"SELECT Price FROM items WHERE Restaurant = '{Order.calculatePrice[1]}' AND Name2 = '{Order.calculatePrice[0]}'")
                myresult = mycursor.fetchall()
                for x in myresult:
                    price=4 * x[0]
                    Order.totalPrice(update, context,price)
                    Order.total_food_to_be_ordered.append(f"4 x {x[0]} = {price} ብር")

                sql = f"UPDATE `{username}` SET calculatePrice = '4 x {x[0]} = {price} ብር' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

                sql = f"UPDATE `{username}` SET price = '{price}' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

        for x in checker:
            if x[0] == "English":
                NumberOfFood.numberoffood(update, context)
            else:
                NumberOfFood.numberoffoodAmharic(update, context)

    elif "5" in update.message.text:
        telegramUserName=update['message']['chat']['first_name']
        username=telegramUserName.lower()+" basket"
        for x in checker:
            if x[0] == "English":
                mycursor = db.mydb.cursor()
                mycursor.execute(f"SELECT Price FROM items WHERE Restaurant = '{Order.calculatePrice[1]}' AND Name1 = '{Order.calculatePrice[0]}'")
                myresult = mycursor.fetchall()
                for x in myresult:
                    price=5 * x[0]
                    Order.totalPrice(update, context,price)
                    Order.total_food_to_be_ordered.append(f"5 x {x[0]} = {price} Birr")

                sql = f"UPDATE `{username}` SET calculatePrice = '5 x {x[0]} = {price} Birr' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

                sql = f"UPDATE `{username}` SET price = '{price}' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

            else:
                mycursor = db.mydb.cursor()
                mycursor.execute(f"SELECT Price FROM items WHERE Restaurant = '{Order.calculatePrice[1]}' AND Name2 = '{Order.calculatePrice[0]}'")
                myresult = mycursor.fetchall()
                for x in myresult:
                    price=5 * x[0]
                    Order.totalPrice(update, context,price)
                    Order.total_food_to_be_ordered.append(f"5 x {x[0]} = {price} ብር")

                sql = f"UPDATE `{username}` SET calculatePrice = '5 x {x[0]} = {price} ብር' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

                sql = f"UPDATE `{username}` SET price = '{price}' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

        for x in checker:
            if x[0] == "English":
                NumberOfFood.numberoffood(update, context)
            else:
                NumberOfFood.numberoffoodAmharic(update, context)

    elif "6" in update.message.text:
        telegramUserName=update['message']['chat']['first_name']
        username=telegramUserName.lower()+" basket"
        for x in checker:
            if x[0] == "English":
                mycursor = db.mydb.cursor()
                mycursor.execute(f"SELECT Price FROM items WHERE Restaurant = '{Order.calculatePrice[1]}' AND Name1 = '{Order.calculatePrice[0]}'")
                myresult = mycursor.fetchall()
                for x in myresult:
                    price=6 * x[0]
                    Order.totalPrice(update, context,price)
                    Order.total_food_to_be_ordered.append(f"6 x {x[0]} = {price} Birr")
                sql = f"UPDATE `{username}` SET calculatePrice = '6 x {x[0]} = {price} Birr' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

                sql = f"UPDATE `{username}` SET price = '{price}' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

            else:
                mycursor = db.mydb.cursor()
                mycursor.execute(f"SELECT Price FROM items WHERE Restaurant = '{Order.calculatePrice[1]}' AND Name2 = '{Order.calculatePrice[0]}'")
                myresult = mycursor.fetchall()
                for x in myresult:
                    price=6 * x[0]
                    Order.totalPrice(update, context,price)
                    Order.total_food_to_be_ordered.append(f"6 x {x[0]} = {price} ብር")
                sql = f"UPDATE `{username}` SET calculatePrice = '6 x {x[0]} = {price} ብር' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

                sql = f"UPDATE `{username}` SET price = '{price}' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

        for x in checker:
            if x[0] == "English":
                NumberOfFood.numberoffood(update, context)
            else:
                NumberOfFood.numberoffoodAmharic(update, context)

    elif "7" in update.message.text:
        telegramUserName=update['message']['chat']['first_name']
        username=telegramUserName.lower()+" basket"
        for x in checker:
            if x[0] == "English":
                mycursor = db.mydb.cursor()
                mycursor.execute(f"SELECT Price FROM items WHERE Restaurant = '{Order.calculatePrice[1]}' AND Name1 = '{Order.calculatePrice[0]}'")
                myresult = mycursor.fetchall()
                for x in myresult:
                    price=7 * x[0]
                    Order.totalPrice(update, context,price)
                    Order.total_food_to_be_ordered.append(f"7 x {x[0]} = {price} Birr")
                sql = f"UPDATE `{username}` SET calculatePrice = '7 x {x[0]} = {price} Birr' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

                sql = f"UPDATE `{username}` SET price = '{price}' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

            else:
                mycursor = db.mydb.cursor()
                mycursor.execute(f"SELECT Price FROM items WHERE Restaurant = '{Order.calculatePrice[1]}' AND Name2 = '{Order.calculatePrice[0]}'")
                myresult = mycursor.fetchall()
                for x in myresult:
                    price=7 * x[0]
                    Order.totalPrice(update, context,price)
                    Order.total_food_to_be_ordered.append(f"7 x {x[0]} = {price} ብር")
                sql = f"UPDATE `{username}` SET calculatePrice = '7 x {x[0]} = {price} ብር' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

                sql = f"UPDATE `{username}` SET price = '{price}' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

        for x in checker:
            if x[0] == "English":
                NumberOfFood.numberoffood(update, context)
            else:
                NumberOfFood.numberoffoodAmharic(update, context)

    elif "8" in update.message.text:
        telegramUserName=update['message']['chat']['first_name']
        username=telegramUserName.lower()+" basket"
        for x in checker:
            if x[0] == "English":
                mycursor = db.mydb.cursor()
                mycursor.execute(f"SELECT Price FROM items WHERE Restaurant = '{Order.calculatePrice[1]}' AND Name1 = '{Order.calculatePrice[0]}'")
                myresult = mycursor.fetchall()
                for x in myresult:
                    price=8 * x[0]
                    Order.totalPrice(update, context,price)
                    Order.total_food_to_be_ordered.append(f"8 x {x[0]} = {price} Birr")
                sql = f"UPDATE `{username}` SET calculatePrice = '8 x {x[0]} = {price} Birr' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

                sql = f"UPDATE `{username}` SET price = '{price}' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

            else:
                mycursor = db.mydb.cursor()
                mycursor.execute(f"SELECT Price FROM items WHERE Restaurant = '{Order.calculatePrice[1]}' AND Name2 = '{Order.calculatePrice[0]}'")
                myresult = mycursor.fetchall()
                for x in myresult:
                    price=8 * x[0]
                    Order.totalPrice(update, context,price)
                    Order.total_food_to_be_ordered.append(f"8 x {x[0]} = {price} ብር")

                sql = f"UPDATE `{username}` SET calculatePrice = '8 x {x[0]} = {price} ብር' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

                sql = f"UPDATE `{username}` SET price = '{price}' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

        for x in checker:
            if x[0] == "English":
                NumberOfFood.numberoffood(update, context)
            else:
                NumberOfFood.numberoffoodAmharic(update, context)

    elif "9" in update.message.text:
        telegramUserName=update['message']['chat']['first_name']
        username=telegramUserName.lower()+" basket"
        for x in checker:
            if x[0] == "English":
                mycursor = db.mydb.cursor()
                mycursor.execute(f"SELECT Price FROM items WHERE Restaurant = '{Order.calculatePrice[1]}' AND Name1 = '{Order.calculatePrice[0]}'")
                myresult = mycursor.fetchall()
                for x in myresult:
                    price=9 * x[0]
                    Order.totalPrice(update, context,price)
                    Order.total_food_to_be_ordered.append(f"9 x {x[0]} = {price} Birr")

                sql = f"UPDATE `{username}` SET calculatePrice = '9 x {x[0]} = {price} Birr' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

                sql = f"UPDATE `{username}` SET price = '{price}' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()


            else:
                mycursor = db.mydb.cursor()
                mycursor.execute(f"SELECT Price FROM items WHERE Restaurant = '{Order.calculatePrice[1]}' AND Name2 = '{Order.calculatePrice[0]}'")
                myresult = mycursor.fetchall()
                for x in myresult:
                    price=9 * x[0]
                    Order.totalPrice(update, context,price)
                    Order.total_food_to_be_ordered.append(f"9 x {x[0]} = {price} ብር")

                sql = f"UPDATE `{username}` SET calculatePrice = '9 x {x[0]} = {price} ብር' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

                sql = f"UPDATE `{username}` SET price = '{price}' WHERE food = '{Order.food_to_be_added_to_database[0]}'"
                mycursor.execute(sql)
                db.mydb.commit()

        for x in checker:
            if x[0] == "English":
                NumberOfFood.numberoffood(update, context)
            else:
                NumberOfFood.numberoffoodAmharic(update, context)


    elif "Amharic" in update.message.text:
        update.message.reply_text(text="ቋንቋው አማርኛ ሆኑአል")
        update.message.reply_text(text="ሙሉ ስምዎን ያስገቡ")

    elif f"{personalInfo[1]}" in update.message.text:
        #print(randomString)
        if personalInfo[0] == "English":
            print("English")
            del personalInfo[0]
            Contact.kuankua.append("English")
            print(f"Contact Kuankua: {Contact.kuankua[0]}")
            Contact.contact_callback(update,context)
        else:
            print("Amharic")
            del personalInfo[0]
            Contact.kuankua.append("Amharic")
            print(f"Contact Kuankua: {Contact.kuankua[0]}")
            Contact.contact_callback(update,context)