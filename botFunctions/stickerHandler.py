# -*- coding: utf-8 -*-
import configuration
import botFunctions

admin = configuration.admin


def privateSticker(bot, message):
    if message.from_user.id == admin and message.reply_to_message is not None:
        try:
            bot.send_sticker(chat_id=message.reply_to_message.forward_from.id, data=message.sticker.file_id)
        except:
            print('Cannot send message to pm user')
        return
    if message.from_user.id != admin:
        bot.send_message(chat_id=admin, text='>>> private sticker send by ' + botFunctions.getName(message.from_user))
        bot.forward_message(chat_id=admin, from_chat_id=message.chat.id, message_id=message.message_id)


def replyToSticker(bot, message, types):
    if botFunctions.isAvailable(message.chat.id, message.reply_to_message.from_user.id):
        try:
            bot.send_message(chat_id=message.reply_to_message.from_user.id,
                             text=botFunctions.getName(
                                 message.from_user) + ' @ <b>' + message.chat.title + '</b> : reply as a Sticker',
                             parse_mode='HTML')
            bot.send_sticker(chat_id=message.reply_to_message.from_user.id, data=message.sticker.file_id)
        except:
            botFunctions.exceptionHandling(message, bot, types, message.from_user)
