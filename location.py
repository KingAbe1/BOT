from telegram.ext import *
from telegram.ext.dispatcher import run_async
from telegram import *
import Responses as R
import restaurantSelection as restaurant
import DatabaseConnector as db
import choice as Choice
import contact as Contact
from datetime import datetime
import basket as Basket
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

print("Opening Selenium")
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com/maps")

count=[0]
food_holder=[]
food_price=[0]
checkers=[]
id=[]
deliveryFee=[0]
totalPrice=[0]
def location(update,context):
    telegramUserName = update['message']['chat']['first_name']
    mycursor = db.mydb.cursor()
    sql =f"Select language FROM clients where userName='{telegramUserName}'"
    mycursor.execute(sql)
    checker = mycursor.fetchall()
    for x in checker:
        if x[0] == "English":
            print("TRUEEEEEEEEEEEEEEEE")
            if len(checkers) == 0:
                checkers.append("Added to database")
                location_keyboard = KeyboardButton(text="Share my location",  request_location=True)
                custom_keyboard = [[ location_keyboard]]
                reply_markup = ReplyKeyboardMarkup(custom_keyboard,resize_keyboard=True,one_time_keyboard=True)
                update.message.reply_text("Please turn on your device location and press the share my location button below.",reply_markup=reply_markup)
            else:
                print("ANOTHER")
                message = update.message
                current_pos = (message.location.latitude, message.location.longitude)

                telegramUserName = update['message']['chat']['first_name']

                mycursor = db.mydb.cursor()
                mycursor.execute(f"SELECT id FROM clients WHERE userName='{telegramUserName}'")
                result = mycursor.fetchall()
                for x in result:
                    id.append(x[0])

                username=telegramUserName.lower()+" basket"
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

                    direction = driver.find_element_by_id("xoLGzf-T3iPGc")
                    direction.send_keys(Keys.RETURN)


                    try:
                        your_location = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.XPATH,"//div[@id='sb_ifc51']/input[1]"))
                        )
                        driver.find_element_by_xpath("//div[@id='sb_ifc51']/input[1]").clear()
                        your_location.send_keys(f"{current_pos[0]},{current_pos[1]}")

                        your_Destination = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.XPATH,"//div[@id='sb_ifc52']/input[1]"))
                        )
                        your_Destination.send_keys(f"{Basket.resturant_name[0].title()}")
                        your_Destination.send_keys(Keys.RETURN)

                        detail = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.ID,"section-directions-trip-details-msg-0"))
                        )
                        driver.find_element_by_id("section-directions-trip-details-msg-0").click()

                        km = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, "html/body/div[3]/div[9]/div[8]/div/div/div/div/div[3]/div/h1/span/span[2]/span"))
                        )
                        dis = driver.find_element_by_xpath("html/body/div[3]/div[9]/div[8]/div/div/div/div/div[3]/div/h1/span/span[2]/span").text
                        print(f"Diatance: {dis}")
                        distance = dis.replace('km','')
                        distance = distance.strip()

                    except:
                        print("Exception Error")

                    mycursor = db.mydb.cursor()
                    mycursor.execute(f"SELECT Distance,Price FROM deliverfee")
                    result = mycursor.fetchall()
                    for x in result:
                        distanceInString = x[0]
                        if len(distanceInString) == 3:
                            if float(distance) >= int(distanceInString[0]) and float(distance) < int(distanceInString[2]):
                                deliveryFee[0] = x[1]
                                break

                        elif len(distanceInString) == 4:
                            if float(distance) >= int(distanceInString[0]) and float(distance) < (int(f"{distanceInString[2]}{distanceInString[3]}")):
                                deliveryFee[0] = x[1]
                                break

                        elif len(distanceInString) == 5:
                            if float(distance) >= int(distanceInString[0]) and float(distance) < (int(f"{distanceInString[3]}{distanceInString[4]}")):
                                deliveryFee[0] = x[1]
                                break

                    totalPrice[0] = int(deliveryFee[0]) + food_price[0]
                    newline="\n"
                    reply_markup = InlineKeyboardMarkup(keyboard)
                    print(food_holder)

                    update.message.reply_text(f"Order\n\n👤 ID: {id[0]}\n\nResturant: {Basket.resturant_name[0].title()}\n\nFoods:\n\n{newline.join(str(x) for x in food_holder)}\n\nTotal Food Price: {food_price[0]} Birr\n🚚 Delivery Fee: {int(deliveryFee[0])} Birr\n💵 Total Price: {totalPrice[0]} Birr",reply_markup=reply_markup)

                    id.pop()
                    totalPrice[0] = 0
                    food_price[0] = 0
                    # deliveryFee[0] = 0

                    keyboard = [['🚖 Order it', '🙀 Maybe later'],['Restart the bot']]
                    message = "If your sure you want to order the food please click 🚖 Order it button if your not sure please click 🙀 Maybe later button"
                    reply_markup = ReplyKeyboardMarkup(keyboard,one_time_keyboard=True,resize_keyboard=True)
                    update.message.reply_text(message, reply_markup=reply_markup)

                    driver.back()
                    driver.back()
                    checkers.pop()

        else:
            if len(checkers) == 0:
                checkers.append("Added to database")
                location_keyboard = KeyboardButton(text="አካባቢዎን ይላኩ",  request_location=True)
                custom_keyboard = [[ location_keyboard]]
                reply_markup = ReplyKeyboardMarkup(custom_keyboard,resize_keyboard=True,one_time_keyboard=True)
                update.message.reply_text("እባክዎን የስልክዎን ሎኬሽን ያብሩ እና ከስር የሚታየውን አካባቢዎን ይላኩ የሚለውን ቁልፍ ይጫኑ።",reply_markup=reply_markup)
            else:
                message = update.message
                current_pos = (message.location.latitude, message.location.longitude)

                telegramUserName = update['message']['chat']['first_name']

                mycursor = db.mydb.cursor()
                mycursor.execute(f"SELECT id FROM clients WHERE userName='{telegramUserName}'")
                result = mycursor.fetchall()
                for x in result:
                    id.append(x[0])

                username=telegramUserName.lower()+" basket"
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

                    direction = driver.find_element_by_id("xoLGzf-T3iPGc")
                    direction.send_keys(Keys.RETURN)

                    try:
                        your_location = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.XPATH,"//div[@id='sb_ifc51']/input[1]"))
                        )
                        driver.find_element_by_xpath("//div[@id='sb_ifc51']/input[1]").clear()
                        your_location.send_keys(f"{current_pos[0]},{current_pos[1]}")

                        your_Destination = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.XPATH,"//div[@id='sb_ifc52']/input[1]"))
                        )
                        your_Destination.send_keys(f"{Basket.resturant_name[0].title()}")
                        your_Destination.send_keys(Keys.RETURN)

                        detail = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.ID,"section-directions-trip-details-msg-0"))
                        )
                        driver.find_element_by_id("section-directions-trip-details-msg-0").click()

                        km = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, "html/body/div[3]/div[9]/div[8]/div/div/div/div/div[3]/div/h1/span/span[2]/span"))
                        )
                        dis = driver.find_element_by_xpath("html/body/div[3]/div[9]/div[8]/div/div/div/div/div[3]/div/h1/span/span[2]/span").text
                        print(f"Distance: {dis}")
                        distance = dis.replace('km','')
                        print(f"Distance: {distance}")
                        distance = distance.strip()
                        distance = int(distance)
                        print(f"Dist: {distance}")

                    except:
                        print("Exception Error")

                    mycursor = db.mydb.cursor()
                    mycursor.execute(f"SELECT Distance,Price FROM deliverfee")
                    result = mycursor.fetchall()
                    for x in result:
                        distanceInString = x[0]
                        if len(distanceInString) == 3:
                            if float(distance) >= int(distanceInString[0]) and float(distance) < int(distanceInString[2]):
                                deliveryFee[0] = x[1]
                                break

                        elif len(distanceInString) == 4:
                            if float(distance) >= int(distanceInString[0]) and float(distance) < (int(f"{distanceInString[2]}{distanceInString[3]}")):
                                deliveryFee[0] = x[1]
                                break

                        elif len(distanceInString) == 5:
                            if float(distance) >= int(distanceInString[0]) and float(distance) < (int(f"{distanceInString[3]}{distanceInString[4]}")):
                                deliveryFee[0] = x[1]
                                print(f"Deliver Fee: {deliveryFee[0]}")
                                break

                    totalPrice[0] = int(deliveryFee[0]) + food_price[0]
                    newline="\n"
                    reply_markup = InlineKeyboardMarkup(keyboard)
                    print(food_holder)

                    update.message.reply_text(f"ትዕዛዝ\n\n👤 መታወቂያ ቁጥር: {id[0]}\n\nምግብ ቤት: {Basket.resturant_name[0].title()}\n\nምግቦች:\n\n{newline.join(str(x) for x in food_holder)}\n\nጠቅላላ የምግብ ዋጋ: {food_price[0]} ብር\n🚚 የመላኪያ ክፍያ: {int(deliveryFee[0])} ብር\n💵 ጠቅላላ ዋጋ: {totalPrice[0]} ብር",reply_markup=reply_markup)

                    id.pop()
                    totalPrice[0] = 0
                    food_price[0] = 0
                    # deliveryFee[0] = 0

                    keyboard = [['🚖 ይዘዙት', '🙀 ምናልባት በኋላ'],['ቦቱን እንደገና ያስጀምሩ']]
                    message = "ምግቡን ማዘዝ እንደሚፈልጉ እርግጠኛ ከሆኑ እባክዎን 🚖 ይዘዙት የሚለውን ክሊክ ያድርጉ እርግጠኛ ካልሆኑ 🙀 ምናልባት በኋላ የሚለውን ክሊክ ያድርጉ"
                    reply_markup = ReplyKeyboardMarkup(keyboard,one_time_keyboard=True,resize_keyboard=True)
                    update.message.reply_text(message, reply_markup=reply_markup)

                    driver.back()
                    driver.back()
                    checkers.pop()