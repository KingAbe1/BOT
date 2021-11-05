from telegram.ext import *
from telegram import *
import DatabaseConnector as db
import datetime
import menu as Menu
import order as Order
import basket as Basket
import location as LOCATION
import time
import restaurantSelection as Restaurant

item = []
quantity = [0]
price = [0]
tableRes = []
id = []
name = []
phoneNumber = []
numberOfOrder = []
def confirmation(update,context):
    telegramUserName = update['message']['chat']['first_name']
    username = telegramUserName.lower()+" basket"

    now = datetime.datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    print(formatted_date)

    mycursor = db.mydb.cursor()
    mycursor.execute(f"SELECT id,fullName,phoneNumber FROM clients WHERE userName='{telegramUserName}'")
    result = mycursor.fetchall()
    for x in result:
        id.append(x[0])
        name.append(x[1])
        phoneNumber.append(x[2])

    mycursor = db.mydb.cursor()
    mycursor.execute(f"SELECT food,calculatePrice,price FROM `{username}`")
    result = mycursor.fetchall()
    for x in result:
        numberOfOrder = x[1]

    mycursor = db.mydb.cursor()
    mycursor.execute(f"SELECT food,calculatePrice,price FROM `{username}`")
    history = mycursor.fetchall()
    for x in history:
        NoOrder = x[1]
        quantity[0] = quantity[0] + int(NoOrder[0])
        item.append(x[0])
        price[0] = price[0] + int(x[2])

    newline="\n"

    mycursor = db.mydb.cursor()
    sql =f"INSERT INTO orders(Customer_Id,Customer_Name,Customer_Phone,Restaurant,Status,Item_Name,Quantity,price,Date,deliveryFee) values ('{id[0]}','{name[0]}','{phoneNumber[0]}','{tableRes[0]}','Pending','{newline.join(str(x) for x in LOCATION.food_holder)}','{quantity[0]}','{price[0]}','{formatted_date}','{LOCATION.deliveryFee[0]}')"
    mycursor.execute(sql)
    db.mydb.commit()

    tableRes.pop()
    id.pop()
    name.pop()
    phoneNumber.pop()

    price[0] = 0
    quantity[0] = 0


    telegramUserName = update['message']['chat']['first_name']
    username = telegramUserName.lower()+" basket"

    mycursor = db.mydb.cursor()
    sql = f"DROP TABLE `{username}`"
    mycursor.execute(sql)
    db.mydb.commit()


    i = 0

    while(i < len(Order.food_to_be_added_to_database)):
        Order.food_to_be_added_to_database.pop()

    while(i<len(Menu.table_forMenu)):
        Menu.table_forMenu.pop()

    while(i<len(Order.total_food_to_be_ordered)):
        Order.total_food_to_be_ordered.pop()

    while(i<len(Order.overAllPrice)):
        Order.overAllPrice.pop()

    while(i<len(LOCATION.food_holder)):
        LOCATION.food_holder.pop()

    while(i<len(Order.food_to_be_added_to_database)):
        Order.food_to_be_added_to_database.pop()

    while(i<len(item)):
        item.pop()


    update.message.reply_text(text="We will call you to confirm your orders.\nUntil then click this 👉 /status to check the status of your order.")

def confirmationAmharic(update,context):
    telegramUserName = update['message']['chat']['first_name']
    username = telegramUserName.lower()+" basket"

    now = datetime.datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

    mycursor = db.mydb.cursor()
    mycursor.execute(f"SELECT id,fullName,phoneNumber FROM clients WHERE userName='{telegramUserName}'")
    result = mycursor.fetchall()
    for x in result:
        id.append(x[0])
        name.append(x[1])
        phoneNumber.append(x[2])

    mycursor = db.mydb.cursor()
    mycursor.execute(f"SELECT food,calculatePrice,price FROM `{username}`")
    result = mycursor.fetchall()
    for x in result:
        numberOfOrder = x[1]

    mycursor = db.mydb.cursor()
    mycursor.execute(f"SELECT food,calculatePrice,price FROM `{username}`")
    history = mycursor.fetchall()
    for x in history:
        NoOrder = x[1]
        quantity[0] = quantity[0] + int(NoOrder[0])
        item.append(x[0])
        price[0] = price[0] + int(x[2])
        print(f"Price: {price[0]}")

    newline="\n"

    mycursor = db.mydb.cursor()
    sql =f"INSERT INTO orders(Customer_Id,Customer_Name,Customer_Phone,Restaurant,Status,Item_Name,Quantity,price,Date,deliveryFee) values ('{id[0]}','{name[0]}','{phoneNumber[0]}','{tableRes[0]}','Pending','{newline.join(str(x) for x in LOCATION.food_holder)}','{quantity[0]}','{price[0]}','{formatted_date}','{LOCATION.deliveryFee[0]}')"
    mycursor.execute(sql)
    db.mydb.commit()


    update.message.reply_text(text="የእኛን 🤖 ቦት ተጠቅመው ስላዘዙ እናመሰግናለን")

    telegramUserName=update['message']['chat']['first_name']
    username=telegramUserName.lower()+" basket"

    mycursor = db.mydb.cursor()
    sql = f"DROP TABLE `{username}`"
    mycursor.execute(sql)
    db.mydb.commit()

    tableRes.pop()
    id.pop()
    name.pop()
    phoneNumber.pop()

    price[0] = 0
    quantity[0] = 0

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

    while(i<len(LOCATION.food_holder)):
        LOCATION.food_holder.pop()

    # while(i<len(Order.food_to_be_added_to_database)):
    #     Order.food_to_be_added_to_database.pop()

    while(i<len(item)):
        item.pop()

    Restaurant.restaruntSelectionAmharic(update, context)