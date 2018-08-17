# -*- coding: utf-8 -*-
import configuration
import botFunctions

admin = configuration.admin

def privateSticker(bot, message):
    if (message.from_user.id == admin and message.reply_to_message != None):
        try:
            bot.send_sticker(chat_id=message.reply_to_message.forward_from.id, data=message.sticker.file_id)
        except:
            print('Cannot send message to pm user')
        return
    if (message.from_user.id != admin):
        bot.send_message(chat_id=admin, text='>>> private sticker send by ' + botFunctions.getName(message.from_user))
        bot.forward_message(chat_id=admin, from_chat_id=message.chat.id, message_id=message.message_id)