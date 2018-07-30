# -*- coding: utf-8 -*-
import botFunctions
import configuration

admin = configuration.admin

def leftMember(message):
    botFunctions.leftOfKikMember(message.chat.id, message.left_chat_member.id)

def kikBot(bot, message):
    if(botFunctions.kikBotDB(message.chat.id)=='success'):
        bot.send_message(chat_id=admin, text='Successfully kik me from ' + str(message.chat.title) + ' '+ str(message.chat.type) + ' by ' + botFunctions.getName(message.from_user))
    else:
        bot.send_message(chat_id=admin,
                         text='Failed to kik me from ' + str(message.chat.title) + ' '+ str(message.chat.type) + ' by ' + botFunctions.getName(message.from_user))