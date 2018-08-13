# -*- coding: utf-8 -*-
import configuration
import botFunctions
import re
import emojiList

admin = configuration.admin

def addingBot(bot, message):
    if(botFunctions.addToGroup(message.chat.id, message.chat.title)=='success'):
        bot.send_message(chat_id=admin, text='Successfully Added me for <b>' + message.chat.title + '</b> ' + message.chat.type + ' and added me by ' + botFunctions.getName(message.from_user) + " " + emojiList.successFaceIcon, parse_mode='HTML')
        try:
            bot.send_message(chat_id=message.chat.id, text='Thank you '+ botFunctions.getName(message.from_user) + ' for adding me to <b>' + message.chat.title + '</b> ' + message.chat.type + '. All the group details and user details are successfully added to the database. ' + emojiList.successFaceIcon, parse_mode='HTML')
        except:
            bot.send_message(chat_id=admin, text='Failed to send welcome message for <b>' + message.chat.title + '</b> ' +message.chat.type + ' and added me by ' + botFunctions.getName(message.from_user) + " " + emojiList.failFaceIcon,parse_mode='HTML')
    else:
        bot.send_message(chat_id=admin, text='Failed to Add bot for ' + message.chat.title + ' ' + message.chat.type + '. Try to added me by ' + botFunctions.getName(message.from_user) + " " + emojiList.failFaceIcon)
        bot.leave_chat(chat_id=message.chat.id)

    adminList = []
    failedDic = {}
    for chat in bot.get_chat_administrators(message.chat.id):
        if(chat.user.is_bot==False):
            adminList.append(chat.user.id)
            if(botFunctions.addToAllUser(chat.user)=="success"):
                failedDic[str(chat.user.id)] = botFunctions.getName(chat.user)
            botFunctions.addToUser(message.chat.id, chat.user.id)

    if(failedDic!={}):
        for admn in adminList:
            if(str(admn) not in list(failedDic.keys())):
                for nm in list(failedDic.values()):
                    try:
                        bot.send_message(chat_id=admn, text='<b>Tell</b> ' + nm + ' <b>to START me in privately. This is important, otherwise I cannot send message to</b> ' + nm + " " + emojiList.failFaceIcon, parse_mode='HTML')
                    except:
                        print("Failed to send message to the admin")

def getOtherAdmins(bot, message):
    adminMessage = "<b>BOT Added to the Group by an Unauthorized Person</b>" + emojiList.exclamationMarkIcon + "\n\nGroup Title : <b>" + message.chat.title + "</b> (" + str(
        message.chat.id) + ")\nGroup Members Count : " + str((bot.get_chat_members_count(
        chat_id=message.chat.id)) - 1) + "\nGroup Type : " + message.chat.type + "\nCreator & Admins : \n\n"

    for admin in bot.get_chat_administrators(chat_id=message.chat.id):
        adminMessage = adminMessage + botFunctions.setupFullName(admin.user) + ' - ' + admin.status + '\n'

    bot.send_message(chat_id=message.chat.id,
                     text= botFunctions.getName(message.from_user) + ' you have <b>no permission</b> to add me to ' + message.chat.title + ' ' + message.chat.type + '. It will be <b>reported</b> to creator of this Bot\n\nThank You', parse_mode='HTML')
    bot.leave_chat(chat_id=message.chat.id)

    adminMessage = adminMessage + "\nAdded me by " + botFunctions.getName(message.from_user)
    bot.send_message(chat_id=configuration.admin, text=adminMessage, parse_mode='HTML')

def addingUser(bot, message, types):
    botFunctions.addToUser(message.chat.id, message.new_chat_member.id)
    if(botFunctions.addToAllUser(message.new_chat_member)=='failed'):
        botFunctions.updateToAllUser(message.new_chat_member)
    else:
        try:
            bot.send_message(chat_id=message.from_user.id, text='<b>Tell</b> ' + botFunctions.getName(message.new_chat_member) + ' <b>to START me in privately. This is important, otherwise I cannot send message to</b> '+ botFunctions.getName(message.new_chat_member) + " " + emojiList.failFaceIcon,  parse_mode='HTML')
            botFunctions.exceptionHandling(message, bot, types, message.new_chat_member)
        except:
            print('Cannot send message to admin')

def welcomeToUser(bot, meessage):
    welcomeMessage = botFunctions.getWelcomeMessage(meessage.chat.id)

    p = re.compile('(#uname)')
    welcomeMessage = p.sub("@"+str(meessage.new_chat_member.username), welcomeMessage)
    p = re.compile('(#fname)')
    welcomeMessage = p.sub(str(meessage.new_chat_member.first_name), welcomeMessage)
    p = re.compile('(#lname)')
    welcomeMessage = p.sub(str(meessage.new_chat_member.last_name), welcomeMessage)
    p = re.compile('(#title)')
    welcomeMessage = p.sub(str(meessage.chat.title), welcomeMessage)

    try:
        bot.send_message(chat_id=meessage.chat.id, text=welcomeMessage, parse_mode='HTML')
    except:
        print("welcome message sending failed")

def checkAndAdd(bot, message):
    if (botFunctions.isUserSuperAdmin(message.from_user.id)):
        addingBot(bot, message)
    else:
        getOtherAdmins(bot, message)