from telegram.ext import *
from telegram import *
import DatabaseConnector as db
import menu as Menu

food_to_be_added_to_database=[]
overAllPrice=[]
calculatePrice=[]
total_food_to_be_ordered=[]
table_forMenu=[]
orderFood=[]
numberOfFoodToOrder=[]

def order(update,context,foodName):
    telegramUserName=update['message']['chat']['first_name']
    username=telegramUserName.lower()+" basket"

    mycursor = db.mydb.cursor()
    mycursor.execute(f"SHOW TABLES LIKE '%{username}%'")
    myresult = mycursor.fetchall()

    if (len(myresult) > 0):
        mycursor = db.mydb.cursor()
        mycursor.execute(f"SELECT COUNT(food) FROM `{username}` WHERE food = '{foodName}'")
        myresult = mycursor.fetchall()
        for x in myresult:
            if x[0] == 0:
                food_to_be_added_to_database.append(foodName)
                mycursor = db.mydb.cursor()
                sql=f"INSERT INTO `{username}` (food) VALUES ('{foodName}')"
                mycursor.execute(sql)
                db.mydb.commit()
        food_to_be_added_to_database.append(foodName)

    else:
        food_to_be_added_to_database.append(foodName)

        mycursor = db.mydb.cursor()
        mycursor.execute(f"CREATE TABLE `{username}` (id INT AUTO_INCREMENT PRIMARY KEY, food VARCHAR(255), calculatePrice VARCHAR(255), price VARCHAR(255))")

        mycursor = db.mydb.cursor()
        sql=f"INSERT INTO `{username}` (food) VALUES ('{foodName}')"
        mycursor.execute(sql)
        db.mydb.commit()

    table_name_from_menu=Menu.table[0]

    if (len(orderFood)==0 and len(table_forMenu)==0):
        total_food_to_be_ordered.append(foodName)
        orderFood.append(foodName)
        calculatePrice.append(foodName)
        table_forMenu.append(table_name_from_menu)
        calculatePrice.append(table_name_from_menu)
    else:
        total_food_to_be_ordered.append(foodName)
        orderFood.pop()
        calculatePrice.pop()
        calculatePrice.pop()
        table_forMenu.pop()
        orderFood.append(foodName)
        table_forMenu.append(table_name_from_menu)
        calculatePrice.append(foodName)
        calculatePrice.append(table_name_from_menu)

    chat_id = update['message']['chat']['id']
    mycursor = db.mydb.cursor()
    mycursor.execute(f"SELECT Price,image FROM items WHERE Restaurant = '{table_name_from_menu}' AND Name1 = '{orderFood[0]}'")
    myresult = mycursor.fetchall()
    for x in myresult:
        keyboard = [['1', '2'],['3', '4'],['5', '6'],['7', '8'],['9'],['back','Restart the bot']]
        reply_markup = ReplyKeyboardMarkup(keyboard,one_time_keyboard=True,resize_keyboard=True)
        message = context.bot.sendPhoto(chat_id=chat_id, photo=open(f'C:\\xampp\\htdocs\\EthiomallBot\\image\\{x[1]}', 'rb'), caption=f'{orderFood[0]} 👉 Price: {x[0]} Birr\n\nHow much {orderFood[0]} do you want to order? Choose from keyboards',reply_markup=reply_markup)
        update.message.reply_text(message)



def orderAmharic(update,context,foodName):
    telegramUserName=update['message']['chat']['first_name']
    username=telegramUserName.lower()+" basket"

    mycursor = db.mydb.cursor()
    mycursor.execute(f"SHOW TABLES LIKE '%{username}%'")
    myresult = mycursor.fetchall()

    if (len(myresult) > 0):
        mycursor = db.mydb.cursor()
        mycursor.execute(f"SELECT COUNT(food) FROM `{username}` WHERE food = '{foodName}'")
        myresult = mycursor.fetchall()
        for x in myresult:
            #print(f"COUNT FOOD: {x[0]}")
            if x[0] == 0:
                food_to_be_added_to_database.append(foodName)
                mycursor = db.mydb.cursor()
                sql=f"INSERT INTO `{username}` (food) VALUES ('{foodName}')"
                mycursor.execute(sql)
                db.mydb.commit()
        food_to_be_added_to_database.append(foodName)

    else:

        food_to_be_added_to_database.append(foodName)

        mycursor = db.mydb.cursor()
        mycursor.execute(f"CREATE TABLE `{username}` (id INT AUTO_INCREMENT PRIMARY KEY, food VARCHAR(255), calculatePrice VARCHAR(255), price VARCHAR(255))")

        mycursor = db.mydb.cursor()
        sql=f"INSERT INTO `{username}` (food) VALUES ('{foodName}')"
        mycursor.execute(sql)
        db.mydb.commit()

    table_name_from_menu=Menu.table[0]

    if (len(orderFood)==0 and len(table_forMenu)==0):
        total_food_to_be_ordered.append(foodName)
        orderFood.append(foodName)
        calculatePrice.append(foodName)
        table_forMenu.append(table_name_from_menu)
        calculatePrice.append(table_name_from_menu)
    else:
        total_food_to_be_ordered.append(foodName)
        orderFood.pop()
        calculatePrice.pop()
        calculatePrice.pop()
        table_forMenu.pop()
        orderFood.append(foodName)
        table_forMenu.append(table_name_from_menu)
        calculatePrice.append(foodName)
        calculatePrice.append(table_name_from_menu)

    chat_id = update['message']['chat']['id']
    mycursor = db.mydb.cursor()
    mycursor.execute(f"SELECT Price,image FROM items WHERE Restaurant = '{table_name_from_menu}' AND Name2 = '{orderFood[0]}'")
    myresult = mycursor.fetchall()
    for x in myresult:
        keyboard = [['1', '2'],['3', '4'],['5', '6'],['7', '8'],['9'],['ወደ ኋላ ተመለስ','ቦቱን እንደገና ያስጀምሩ']]
        reply_markup = ReplyKeyboardMarkup(keyboard,one_time_keyboard=True,resize_keyboard=True)
        message = context.bot.sendPhoto(chat_id=chat_id, photo=open(f'C:\\xampp\\htdocs\\EthiomallBot\\image\\{x[1]}', 'rb'), caption=f'{orderFood[0]} 👉 ዋጋ: {x[0]} ብር\n\nስንት ነው {orderFood[0]} ማዘዝ የሚፈልጉት?',reply_markup=reply_markup)
        update.message.reply_text(message)

def totalPrice(update,context,price):
        if len(overAllPrice) == 0:
            overAllPrice.append(price)
        else:
            overAllPrice[0]=overAllPrice[0]+price