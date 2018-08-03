# -*- coding: utf-8 -*-
import botFunctions
import ast

crossIcon = u"\u274C"

def superAdminHandler(bot, types, call, status):
    superAdminList = botFunctions.detailsOfSuperAdmins()
    if(superAdminList==[]):
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="No Super Admins")
        botFunctions.adminWindow(bot, types, call.message, True)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    else:
        title = "<b>Super Admin List</b>"
        markup = types.InlineKeyboardMarkup()
        for adminID in superAdminList:
            adminDetails = botFunctions.userDetailFormatter(adminID)
            if(adminID[3]!=''):
                markup.add(types.InlineKeyboardButton(text=adminDetails, url='https://telegram.me/'+adminID[3]+'?start=XXXX'), types.InlineKeyboardButton(text=crossIcon, callback_data="['superadmin',"+str(adminID[0])+"]"))
            else:
                markup.add(types.InlineKeyboardButton(text=adminDetails,  callback_data='noUserName'), types.InlineKeyboardButton(text=crossIcon, callback_data="['superadmin',"+str(adminID[0])+"]"))
        markup.add(types.InlineKeyboardButton("< back", callback_data="backToHome"))
        if(status):
            bot.edit_message_text(chat_id=call.message.chat.id, text=title, message_id=call.message.message_id, reply_markup=markup, parse_mode='HTML')
        else:
            bot.send_message(chat_id=call.message.chat.id, text=title, reply_markup=markup, parse_mode='HTML')

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

def groupHandler(bot, types, call, status):
    title = "<b>Group List</b>"
    markup = types.InlineKeyboardMarkup()
    groupList = botFunctions.getGroupIDTitle()
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
        successMessage = "Group Successfully Deleted"
    else:
        successMessage = "Group Deletion Failed"
    bot.leave_chat(chat_id=removeID)
    bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=successMessage)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
    groupHandler(bot, types, call, False)

def viewGroupInfo(bot, types, call):
    groupTypeIcon = u"\U0001F4E2"
    descriptionIcon = u"\U0001F4CB"
    memberCountIcon = u"\U0001F468\u200D\U0001F469\u200D\U0001F467\u200D\U0001F466"
    creatorIcon = u"\U0001F920"
    adminIcon = u"\U0001F60E"
    botIcon = u"\U0001F916"
    adminDetails = """"""
    groupID = ast.literal_eval(call.data)[1]
    allDetails = bot.get_chat(groupID)
    if(allDetails.description==None):
        description = "No Description"
    else:
        description = allDetails.description
    for admin in bot.get_chat_administrators(groupID):
        adminList = [admin.user.id, admin.user.first_name, admin.user.last_name, admin.user.username]
        if(admin.status=='creator'):
            creatorDetails = """\t\t\t"""+creatorIcon+""" Creator : """+botFunctions.jsonUserDetailFormatter(adminList)+""""""
        else:
            if(admin.user.is_bot==False):
                adminDetails = adminDetails + """\n\t\t\t"""+adminIcon+""" Administrator : """+botFunctions.jsonUserDetailFormatter(adminList)+""""""
            else:
                adminDetails = adminDetails + """\n\t\t\t""" + botIcon + """ Administrator : """ + botFunctions.jsonUserDetailFormatter(adminList) + """"""
    groupDetails = """<b>"""+ allDetails.title +"""</b>
    
"""+groupTypeIcon+""" Type : """+allDetails.type+"""
"""+descriptionIcon+""" DescriptionIcon : """ + description + """
"""+memberCountIcon+""" Member Count : """ + str(bot.get_chat_members_count(groupID)) + """
Chat Administrators : 
"""+creatorDetails+"""
"""+adminDetails+"""
"""
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("< back", callback_data="groups"), types.InlineKeyboardButton(text=crossIcon, callback_data="['group'," + str(groupID) + "]"))
    bot.edit_message_text(chat_id=call.message.chat.id, text=groupDetails, message_id=call.message.message_id, reply_markup=markup, parse_mode='HTML')