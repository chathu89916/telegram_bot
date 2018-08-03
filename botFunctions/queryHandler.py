# -*- coding: utf-8 -*-
import botFunctions
import ast

def superAdminHandler(bot, types, call, status):
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
    if(status):
        bot.edit_message_text(chat_id=call.message.chat.id, text="<b>Super Admin List</b>", message_id=call.message.message_id, reply_markup=markup, parse_mode='HTML')
    else:
        bot.send_message(chat_id=call.message.chat.id, text="<b>Super Admin List</b>", reply_markup=markup, parse_mode='HTML')

def removeSuperAdmin(bot, types, call):
    removeID = ast.literal_eval(call.data)[1]
    if(botFunctions.removeFromSuperAdmin(removeID)):
        successMessage = "Super Admin Successfully Deleted"
    else:
        successMessage = "Super Admin Deletion Failed"
    bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=successMessage)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id-1)
    superAdminHandler(bot, types, call, False)

def groupHandler():
    pass