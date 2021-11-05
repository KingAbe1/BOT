from telegram.ext import *
from telegram import *
import Responses as R
import restaurantSelection as restaurant
import DatabaseConnector as db
import choice as Choice

nameAndPhoneNumberArr=[]
kuankua = []
def contact_callback(update,context):
    print(f"Kunakua: {kuankua[0]}")
    if kuankua[0] == "English":
        if len(R.personalInfo) == 1:
            R.personalInfo.append("hello")
            con_keyboard = KeyboardButton(text="Phone number", request_contact=True)
            custom_keyboard = [[con_keyboard]]
            reply_markup = ReplyKeyboardMarkup(custom_keyboard,resize_keyboard=True,one_time_keyboard=True)

            message=update.message.reply_text(text='Press Phone number 👇 in order to save your contact number',reply_markup=reply_markup)

        elif len(R.personalInfo)==2:
            contact = update.effective_message.contact
            phone = contact.phone_number

            R.personalInfo[1]=phone
            nameAndPhoneNumberArr.extend(R.personalInfo)
            print(nameAndPhoneNumberArr)
            print("Phone number: "+phone)


            telegramUserName=update['message']['chat']['first_name']
            mycursor = db.mydb.cursor()
            #sql = f"UPDATE user SET fullName = '{nameAndPhoneNumberArr[0]}', phoneNumber = '{nameAndPhoneNumberArr[1]}' WHERE userName = '{telegramUserName}'"
            sql =f"Insert INTO clients(userName,fullName,phoneNumber,language) values ('{telegramUserName}','{nameAndPhoneNumberArr[0]}','{nameAndPhoneNumberArr[1]}','English')"
            mycursor.execute(sql)
            db.mydb.commit()
            print("Record Inserted")


            message=update.message.reply_text("Thank you "+nameAndPhoneNumberArr[0]+" for registering to our bot.")
            Choice.choice(update,context)
            kuankua.pop()

    else:
        # def contact_callbackAmharic(update,context):
        print("Inside contact callback Amharic")
        if len(R.personalInfo) == 1:
            R.personalInfo.append("hello")
            con_keyboard = KeyboardButton(text="ስልክ ቁጥር", request_contact=True)
            custom_keyboard = [[con_keyboard]]
            reply_markup = ReplyKeyboardMarkup(custom_keyboard,resize_keyboard=True,one_time_keyboard=True)

            message=update.message.reply_text(text='ስልክ ቁጥርዎን ለማስቀመጥ ከታች ይለውን 👇 የስልክ ቁጥርን ይጫኑ።',reply_markup=reply_markup)

        elif len(R.personalInfo)==2:
            print("Here i come")
            contact = update.effective_message.contact
            phone = contact.phone_number

            R.personalInfo[1]=phone
            nameAndPhoneNumberArr.extend(R.personalInfo)

            telegramUserName=update['message']['chat']['first_name']
            mycursor = db.mydb.cursor()
            sql =f"Insert INTO clients(userName,fullName,phoneNumber,language) values ('{telegramUserName}','{nameAndPhoneNumberArr[0]}','{nameAndPhoneNumberArr[1]}','Amharic')"
            mycursor.execute(sql)
            db.mydb.commit()


            message=update.message.reply_text("አናመሰግናለን "+nameAndPhoneNumberArr[0]+" ወደ ቦታችን ስለተመመዘገቡ.")
            Choice.choiceAmharic(update,context)
            kuankua.pop()
