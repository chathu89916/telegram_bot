# -*- coding: utf-8 -*-
import configuration
import botFunctions
import re
import emojiList
import welcomeMessage

admin = configuration.admin

def checkBotAddingStatus(bot, message):
    groupIDList = botFunctions.getBanGroups()
    if (str(message.chat.id) in groupIDList):
        if(message.from_user.id == configuration.admin):
            botFunctions.removeFromBanGroup(message.chat.id)
            addingBot(bot, message, False)
        else:
            adminMessage = "<b>BOT Added to the Banned Group</b>" + emojiList.exclamationMarkIcon + "\n\n" + botFunctions.structureGroupDetails(
                bot, message.chat.id)
            adminMessage = adminMessage + "\n\nAdded me by " + botFunctions.getName(message.from_user)
            bot.send_message(chat_id=configuration.admin, text=adminMessage, parse_mode='HTML')

            bot.send_message(chat_id=message.chat.id,
                             text="This group is <b>banned</b> by Bot <b>admin</b>. " + emojiList.failFaceIcon + " Please <b>contact</b> the <b>admin if you want</b> me to be added to this group. " + emojiList.successFaceIcon, parse_mode='HTML')
            bot.leave_chat(chat_id=message.chat.id)
    else:
        addingBot(bot, message, True)

def addingBot(bot, message, status):
    if (botFunctions.addToGroup(message.chat.id, message.chat.title) == 'success'):
        if (status):
            bot.send_message(chat_id=admin,
                             text="<b>Successfully Added me for a Group</b>" + emojiList.exclamationMarkIcon + "\n\n" + botFunctions.structureGroupDetails(
                                 bot, message.chat.id) + "\n\nAdded me by " + botFunctions.getName(message.from_user),
                             parse_mode='HTML')
        try:
            bot.send_message(chat_id=message.chat.id, text='Thank you ' + botFunctions.getName(
                message.from_user) + ' for adding me to <b>' + message.chat.title + '</b> ' + message.chat.type + '. All the group details and user details are successfully added to the database. ' + emojiList.successFaceIcon,
                             parse_mode='HTML')
        except:
            bot.send_message(chat_id=admin,
                             text='Failed to send welcome message for <b>' + message.chat.title + '</b> ' + message.chat.type + ' and added me by ' + botFunctions.getName(
                                 message.from_user) + " " + emojiList.failFaceIcon, parse_mode='HTML')
    else:
        bot.send_message(chat_id=admin,
                         text='Failed to Add bot for ' + message.chat.title + ' ' + message.chat.type + '. Try to added me by ' + botFunctions.getName(
                             message.from_user) + " " + emojiList.failFaceIcon)
        bot.leave_chat(chat_id=message.chat.id)

    adminList = []
    failedDic = {}
    for chat in bot.get_chat_administrators(message.chat.id):
        if (chat.user.is_bot == False):
            adminList.append(chat.user.id)
            if (botFunctions.addToAllUser(chat.user) == "success"):
                failedDic[str(chat.user.id)] = botFunctions.getName(chat.user)
            botFunctions.addToUser(message.chat.id, chat.user.id)

    if (failedDic != {}):
        for admn in adminList:
            if (str(admn) not in list(failedDic.keys())):
                for nm in list(failedDic.values()):
                    try:
                        bot.send_message(chat_id=admn,
                                         text='<b>Tell</b> ' + nm + ' <b>to START me in privately. This is important, otherwise I cannot send message to</b> ' + nm + " " + emojiList.failFaceIcon,
                                         parse_mode='HTML')
                    except:
                        print("Failed to send message to the admin")

def getOtherAdmins(bot, message):
    adminMessage = "<b>BOT Added to the Group by an Unauthorized Person</b>" + emojiList.exclamationMarkIcon + "\n\n" + botFunctions.structureGroupDetails(bot, message.chat.id)

    bot.send_message(chat_id=message.chat.id,
                     text= botFunctions.getName(message.from_user) + ' you have <b>no permission</b> to add me to <b>' + message.chat.title + '</b> ' + message.chat.type + " " + emojiList.failFaceIcon +'. It will be <b>reported to creator</b> of this Bot\n\nThank You ' + emojiList.successFaceIcon, parse_mode='HTML')
    bot.leave_chat(chat_id=message.chat.id)

    adminMessage = adminMessage + "\n\nAdded me by " + botFunctions.getName(message.from_user)
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

def welcomeToUser(bot, message, types):
    markup = None

    if(configuration.RsLKID==str(message.chat.id)):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text="Google+", url=configuration.googlePlusURL),
                   types.InlineKeyboardButton(text="Twitter", url=configuration.twitterURL))
        markup.add(types.InlineKeyboardButton(text="Facebook", url=configuration.facebookURL),
                   types.InlineKeyboardButton(text="Telegram Channel", url=configuration.telegramChannelURL))
        markup.add(types.InlineKeyboardButton(text="To START @"+configuration.botUsername, url="https://telegram.me/"+configuration.botUsername+"?start=XXXX"))
        welcomeMsg = welcomeMessage.ResistanceLKMessage(botFunctions.getName(message.new_chat_member))
    else:
        welcomeMsg = botFunctions.getWelcomeMessage(message.chat.id)

        p = re.compile('(#uname)')
        welcomeMsg = p.sub("@"+str(message.new_chat_member.username), welcomeMsg)
        p = re.compile('(#fname)')
        welcomeMsg = p.sub(str(message.new_chat_member.first_name), welcomeMsg)
        p = re.compile('(#lname)')
        welcomeMsg = p.sub(str(message.new_chat_member.last_name), welcomeMsg)
        p = re.compile('(#title)')
        welcomeMsg = p.sub(str(message.chat.title), welcomeMsg)

    try:
        bot.send_message(chat_id=message.chat.id, text=welcomeMsg, reply_markup=markup, parse_mode='HTML')
    except:
        print("welcome message sending failed")

def checkAndAdd(bot, message):
    if (botFunctions.isUserSuperAdmin(message.from_user.id)):
        checkBotAddingStatus(bot, message)
    else:
        getOtherAdmins(bot, message)