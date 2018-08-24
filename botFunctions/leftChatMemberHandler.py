# -*- coding: utf-8 -*-
import botFunctions
import configuration
import emojiList

admin = configuration.admin
botID = configuration.botID


def leftMember(message):
    botFunctions.leftOfKikMember(message.chat.id, message.left_chat_member.id)


def kikBot(bot, message):
    if botFunctions.kikBotDB(message.chat.id) == 'success':
        if botID != message.from_user.id:
            bot.send_message(chat_id=admin,
                             text='Successfully kick me from the <b>' + message.chat.title + '</b> ' + message.chat.type + ' by ' + botFunctions.getName(
                                 message.from_user) + " " + emojiList.successFaceIcon, parse_mode='HTML')
    else:
        bot.send_message(chat_id=admin,
                         text='Failed to kick me from <b>' + message.chat.title + '</b> ' + message.chat.type + ' by ' + botFunctions.getName(
                             message.from_user) + " " + emojiList.failFaceIcon, parse_mode='HTML')
