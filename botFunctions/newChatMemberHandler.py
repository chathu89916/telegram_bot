# -*- coding: utf-8 -*-
import configuration
import botFunctions
import botFunctions
import re

admin = configuration.admin

def addingBot(bot, message):
    if(botFunctions.addToGroup(message.chat.id, message.chat.title)=='success'):
        bot.send_message(chat_id=admin, text='Successfully Added me for ' + str(message.chat.title) + ' ' + str(
            message.chat.type) + ' and added me by ' + botFunctions.getName(message.from_user))
        bot.send_message(chat_id=message.chat.id,
                         text='Thank you '+ botFunctions.getName(message.from_user) + ' for adding me to <b>' + str(message.chat.title) + '</b> ' + str(message.chat.type) + '. All the group details and user details are successfully added to the database.',
                         parse_mode='HTML')
    else:
        bot.send_message(chat_id=admin, text='Failed to Add bot for ' + str(message.chat.title) + ' ' + str(
            message.chat.type) + '. Try to added me by ' + botFunctions.getName(message.from_user))

    for chat in bot.get_chat_administrators(message.chat.id):
        if(chat.user.is_bot==False):
            botFunctions.addToUser(message.chat.id, chat.user.id)

def getOtherAdmins(bot, message):
    adminMessage = "Group Title : " + message.chat.title + " (" + str(
        message.chat.id) + ")\nGroup Members Count : " + str((bot.get_chat_members_count(
        chat_id=message.chat.id)) - 1) + "\nGroup Type : " + message.chat.type + "\nCreator & Admins : \n\n"

    for admin in bot.get_chat_administrators(chat_id=message.chat.id):
        adminMessage = adminMessage + str(admin.user.first_name) + ' ' + str(admin.user.last_name) + ' @' + str(admin.user.username) + ' - ' + str(admin.status) + '\n'

    bot.send_message(chat_id=message.chat.id,
                     text= botFunctions.getName(message.from_user) + ' you have no permission to add me to ' + str(message.chat.title) + ' ' + message.chat.type + '. It will be reported to creator of this Bot\n\nThank You')
    bot.leave_chat(chat_id=message.chat.id)

    adminMessage = adminMessage + "\nAdded me by " + botFunctions.getName(message.from_user)
    bot.send_message(chat_id=configuration.admin, text=adminMessage)

def addingUser(bot, message, types):
    botFunctions.addToUser(message.chat.id, message.new_chat_member.id)
    if(botFunctions.addToAllUser(message.new_chat_member)=='failed'):
        botFunctions.updateToAllUser(message.new_chat_member)
    else:
        try:
            bot.send_message(chat_id=message.from_user.id, text='<b>Tell</b> ' + botFunctions.getName(message.new_chat_member) + ' <b>to START me in privately. This is important, otherwise I cannot send message to</b> '+ botFunctions.getName(message.new_chat_member),  parse_mode='HTML')
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