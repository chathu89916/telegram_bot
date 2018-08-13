# -*- coding: utf-8 -*-
import botFunctions
import ast
import emojiList

def superAdminHandler(bot, types, call, status):
    superAdminList = botFunctions.detailsOfSuperAdmins()
    if(superAdminList==[]):
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="No Super Admins " +emojiList.failFaceIcon)
        botFunctions.adminWindow(bot, types, call.message, True)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    else:
        title = "<b>Super Admin List</b>"
        markup = types.InlineKeyboardMarkup()
        for adminID in superAdminList:
            adminDetails = botFunctions.userDetailFormatter(adminID)
            if(adminID[3]!=''):
                markup.add(types.InlineKeyboardButton(text=adminDetails, url='https://telegram.me/'+adminID[3]+'?start=XXXX'), types.InlineKeyboardButton(text=emojiList.crossIcon, callback_data="['superadmin',"+str(adminID[0])+"]"))
            else:
                markup.add(types.InlineKeyboardButton(text=adminDetails,  callback_data='noUserName'), types.InlineKeyboardButton(text=emojiList.crossIcon, callback_data="['superadmin',"+str(adminID[0])+"]"))
        markup.add(types.InlineKeyboardButton("< back", callback_data="backToHome"))
        if(status):
            bot.edit_message_text(chat_id=call.message.chat.id, text=title, message_id=call.message.message_id, reply_markup=markup, parse_mode='HTML')
        else:
            bot.send_message(chat_id=call.message.chat.id, text=title, reply_markup=markup, parse_mode='HTML')

def removeSuperAdmin(bot, types, call):
    removeID = ast.literal_eval(call.data)[1]
    if(botFunctions.removeFromSuperAdmin(removeID)):
        successMessage = "Super Admin Successfully Deleted " + emojiList.successFaceIcon
    else:
        successMessage = "Super Admin Deletion Failed " + emojiList.failFaceIcon
    bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=successMessage)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id-1)
    superAdminHandler(bot, types, call, False)

def groupHandler(bot, types, call, status):
    title = "<b>Group List</b>"
    markup = types.InlineKeyboardMarkup()
    groupList = botFunctions.getGroupIDTitle()
    if (groupList == []):
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="No Groups " +emojiList.failFaceIcon)
        botFunctions.adminWindow(bot, types, call.message, True)
    else:
        for groupID in groupList:
            markup.add(types.InlineKeyboardButton(text=groupID[1], callback_data="['viewgroup'," + str(groupID[0]) + "]"))
        markup.add(types.InlineKeyboardButton("< back", callback_data="backToHome"))
        if (status):
            bot.edit_message_text(chat_id=call.message.chat.id, text=title,
                                  message_id=call.message.message_id, reply_markup=markup, parse_mode='HTML')
        else:
            bot.send_message(chat_id=call.message.chat.id, text=title, reply_markup=markup,
                             parse_mode='HTML')

def removeGroup(bot, types, call):
    removeID = ast.literal_eval(call.data)[1]
    if (botFunctions.removeFromGroup(removeID)):
        successMessage = "Group Successfully Deleted " + emojiList.successFaceIcon
    else:
        successMessage = "Group Deletion Failed " + emojiList.failFaceIcon
    bot.leave_chat(chat_id=removeID)
    bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=successMessage)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
    groupHandler(bot, types, call, False)

def viewGroupInfo(bot, types, call):
    groupID = ast.literal_eval(call.data)[1]
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("< back", callback_data="groups"), types.InlineKeyboardButton(text=emojiList.crossIcon, callback_data="['group'," + str(groupID) + "]"))
    bot.edit_message_text(chat_id=call.message.chat.id, text=botFunctions.structureGroupDetails(bot, groupID), message_id=call.message.message_id, reply_markup=markup, parse_mode='HTML')