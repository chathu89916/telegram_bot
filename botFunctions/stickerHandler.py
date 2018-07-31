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

def deleteSticker(bot, message):
    if(not(botFunctions.getStickerPermission(message.chat.id))):
        if(botFunctions.isBotAdmin(bot, message)):
            try:
                bot.delete_message(message.chat.id, message.message_id)
            except:
                print('Sticker Delete Failed')
        else:
            adminList = botFunctions.groupAndSuperAdmin(bot, message)
            for chat in adminList:
                try:
                    bot.send_message(chat_id=chat, text='Cannot delete Stickers in <b>' + message.chat.title + '</b>\n* Please make me as an admin or Enable my Delete Message Permission', parse_mode='HTML')
                except:
                    print('failed to send message to group admin')