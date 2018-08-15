# -*- coding: utf-8 -*-
import botFunctions
import ast
import emojiList

def superAdminHandler(bot, types, call, status):
    superAdminList = botFunctions.detailsOfSuperAdmins()
    if(superAdminList==[]):
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="No Super Admins " +emojiList.failFaceIcon)
        botFunctions.adminWindow(bot, types, call.message, True)
        if(status):
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

def removeSuperAdminQuery(bot, types, call):
    removeID = ast.literal_eval(call.data)[1]
    if(botFunctions.removeFromSuperAdmin(removeID)):
        successMessage = "Super Admin Successfully Deleted " + emojiList.successFaceIcon
    else:
        successMessage = "Super Admin Deletion Failed " + emojiList.failFaceIcon
    bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=successMessage)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id-1)
    superAdminHandler(bot, types, call, False)

def allgroupsHandler(bot, types, call, status):
    title = "<b>All Groups</b>\n\n"
    markup = types.InlineKeyboardMarkup()
    allGroupCount = botFunctions.allgroupsDB().__len__()
    allBanedGroupCount = botFunctions.getBanGroups().__len__()
    title = title + emojiList.houseIcon + " All Group Count : " + str(allGroupCount) + "\n" \
                  + emojiList.bannedGroupIcon + " All Banned Group Count : " + str(allBanedGroupCount)
    markup.add(types.InlineKeyboardButton(text="All Groups", callback_data="groups"),
        types.InlineKeyboardButton(text="All Banned Groups", callback_data="bannedgroups"))
    markup.add(types.InlineKeyboardButton("< back", callback_data="backToHome"))
    if(status):
        bot.edit_message_text(chat_id=call.message.chat.id, text=title, message_id=call.message.message_id, reply_markup=markup, parse_mode='HTML')
    else:
        bot.send_message(chat_id=call.chat.id, text=title, reply_markup=markup,
                     parse_mode='HTML')

def bannedGroupHandler(bot, types, call, status):
    title = "<b>Banned Group List</b>"
    markup = types.InlineKeyboardMarkup()
    groupList = botFunctions.getBannedGroupIDTitle()
    if (groupList == []):
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                  text="No Banned Groups " + emojiList.failFaceIcon)
        botFunctions.allgroupsHandler(bot, types, call.message, False)
        if (status):
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    else:
        for groupID in groupList:
            markup.add(
                types.InlineKeyboardButton(text=groupID[1], callback_data="noGroupName"),
                types.InlineKeyboardButton(text=emojiList.crossIcon, callback_data="['sureRemoveBannedGroup',"+str(groupID[0])+"]"))
        markup.add(types.InlineKeyboardButton("< back", callback_data="backToAllGroup"))
        if (status):
            bot.edit_message_text(chat_id=call.message.chat.id, text=title,
                                  message_id=call.message.message_id, reply_markup=markup, parse_mode='HTML')
        else:
            bot.send_message(chat_id=call.message.chat.id, text=title, reply_markup=markup,
                             parse_mode='HTML')

def removeBannedGroup(bot, types, call):
    removeID = ast.literal_eval(call.data)[1]
    if (botFunctions.removeFromBanGroup(removeID)):
        successMessage = "Banned Group Successfully Deleted " + emojiList.successFaceIcon
    else:
        successMessage = "Banned Group Deletion Failed " + emojiList.failFaceIcon
    bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=successMessage)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
    bannedGroupHandler(bot, types, call, False)

def groupHandler(bot, types, call, status):
    title = "<b>Group List</b>"
    markup = types.InlineKeyboardMarkup()
    groupList = botFunctions.getGroupIDTitle()
    if (groupList == []):
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="No Groups " +emojiList.failFaceIcon)
        botFunctions.allgroupsHandler(bot, types, call.message, False)
        if(status):
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    else:
        for groupID in groupList:
            markup.add(types.InlineKeyboardButton(text=groupID[1], callback_data="['viewgroup'," + str(groupID[0]) + "]"))
        markup.add(types.InlineKeyboardButton("< back", callback_data="backToAllGroup"))
        if (status):
            bot.edit_message_text(chat_id=call.message.chat.id, text=title,
                                  message_id=call.message.message_id, reply_markup=markup, parse_mode='HTML')
        else:
            bot.send_message(chat_id=call.message.chat.id, text=title, reply_markup=markup,
                             parse_mode='HTML')

def removeGroup(bot, types, call):
    removeID = ast.literal_eval(call.data)[1]
    botFunctions.addToBanGroup(removeID)
    if (botFunctions.removeFromGroup(removeID)):
        successMessage = "Group Successfully Deleted " + emojiList.successFaceIcon
    else:
        successMessage = "Group Deletion Failed " + emojiList.failFaceIcon
    bot.send_message(chat_id=removeID, text="Sorry, <b>Bot admin</b> has decided to <b>kick</b> me from this group " + emojiList.failFaceIcon, parse_mode='HTML')
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