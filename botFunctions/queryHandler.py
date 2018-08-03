# -*- coding: utf-8 -*-
import botFunctions

def superAdminHandler(bot, types, call):
    crossIcon = u"\u274C"
    markup = types.InlineKeyboardMarkup()
    superAdminList = botFunctions.detailsOfSuperAdmins()
    for adminID in superAdminList:
        adminDetails = botFunctions.userDetailFormatter(adminID)
        if(adminID[3]!=''):
            markup.add(types.InlineKeyboardButton(text=adminDetails, url='https://telegram.me/'+adminID[3]+'?start=XXXX'), types.InlineKeyboardButton(text=crossIcon, callback_data="['superadmin',"+str(adminID[0])+"]"))
        else:
            markup.add(types.InlineKeyboardButton(text=adminDetails,  callback_data='noUserName'), types.InlineKeyboardButton(text=crossIcon, callback_data="['superadmin',"+str(adminID[0])+"]"))
    markup.add(types.InlineKeyboardButton("< back", callback_data="backToHome"))
    bot.edit_message_text(chat_id=call.message.chat.id, text="<b>Super Admin List</b>", message_id=call.message.message_id, reply_markup=markup, parse_mode='HTML')

def groupHandler():
    pass