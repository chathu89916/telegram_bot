# -*- coding: utf-8 -*-
import re
import botFunctions
import configuration

def getName(name):
    if(name.username == None):
        return name.first_name
    else:
        return '@'+name.username

def exceptionHandling(message, bot, types, name):
    inline = types.InlineKeyboardMarkup()
    START = types.InlineKeyboardButton(text='START', callback_data='START')
    inline.row(START)
    bot.send_message(message.chat.id, text='Agent ' + getName(name) +' Click the START button to Activate the @'+str(configuration.botUsername), reply_markup=inline)

def allCheck(text):
    search = re.findall(r'[@][a][l][l]', text, re.I)
    if(len(search)>0):
        return True
    else:
        return False

def checkAdmin(bot, chatID, userID):
    for chat in bot.get_chat_administrators(chatID):
        if(chat.user.id==userID and chat.user.is_bot==False):
            return True
    if(isUserSuperAdmin(userID)):
        return True
    return False

def isUserSuperAdmin(userID):
    if(userID==configuration.admin):
        return True
    for admin in botFunctions.getAdmin():
        if(admin==str(userID)):
            return True
    return False

def mentionedList(groupID, text):
    mentionedList = []
    listAT = re.findall(r'[@]\w*\b', text)
    listAT = list(set(listAT))
    if(len(listAT)>0):
        for uname in listAT:
            username = re.split(r'[@]', uname)[1]
            userID = botFunctions.getMentionedUser(groupID, username.lower())
            if userID != '':
                mentionedList.append(userID)
    listSUB = re.split('\W+', text)
    listSUB = list(set(listSUB))
    if (len(listSUB) > 0):
        for subname in listSUB:
            userID = botFunctions.getSubscribeUser(subname.lower())
            if(len(userID)>0):
                for uID in userID:
                    mentionedList.append(uID)
    mentionedList = list(set(mentionedList))
    finalMentionedUsers = []
    for getAllUsers in botFunctions.getAllUsers(groupID):
        for mentionUsers in mentionedList:
            if(str(getAllUsers)==str(mentionUsers)):
                finalMentionedUsers.append(mentionUsers)
    return finalMentionedUsers

def isBotAdmin(bot, message):
    for getID in bot.get_chat_administrators(message.chat.id):
        if(getID.user.id==configuration.botID):
            if(getID.can_delete_messages):
                return True
    return False

def stringToBoolean(text):
    if(text=='True'):
        return True
    else:
        return False

# def updateGroupID(message):
#     for IDTitle in botFunctions.getGroupIDTitle():
#         if(str(message.chat.id) == IDTitle[0]):
#             botFunctions.updateGroupTitle(message.chat.id, message.chat.title)
#             return
#         if(message.chat.title==IDTitle[1]):
#             botFunctions.updateGroupID(message)

def autoAddDetails(message, bot, types):
    botFunctions.addToUser(message.chat.id, message.from_user.id)
    if (botFunctions.addToAllUser(message.from_user) == 'success'):
        for admin in bot.get_chat_administrators(chat_id=message.chat.id):
            try:
                bot.send_message(chat_id=admin.user.id, text='<b>Tell</b> ' + getName(message.from_user) + ' <b>to START me in privately. This is important, otherwise I cannot send message to</b> '+ getName(message.from_user),  parse_mode='HTML')
            except:
                print('Cannot send message to admin')
        exceptionHandling(message, bot, types, message.from_user)
        return
    botFunctions.updateToAllUser(message.from_user)

def formatUserData(user):
    firstName = ''
    lastName = ''
    userName = ''

    if(user.first_name != '' and user.first_name != None):
        firstName = user.first_name
    if (user.last_name != '' and user.last_name != None):
        lastName = user.last_name
    if (user.username != '' and user.username != None):
        userName = user.username.lower()

    return firstName, lastName, userName