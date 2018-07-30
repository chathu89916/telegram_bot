# -*- coding: utf-8 -*-
import configuration
import botFunctions

admin = configuration.admin

def privatePhoto(bot, message):
    if(message.from_user.id == admin and message.reply_to_message != None):
        try:
            bot.send_photo(chat_id=message.reply_to_message.forward_from.id, photo=message.photo[-1].file_id, caption=message.caption, parse_mode='HTML')
        except:
            print('Cannot send message to pm user')
        return
    if(message.from_user.id != admin):
        bot.forward_message(chat_id=admin, from_chat_id=message.chat.id, message_id=message.message_id)

def mentionAllPhoto(bot, message):
    if (botFunctions.checkAdmin(bot, message.chat.id, message.from_user.id)):
        if(message.chat.type != 'private'):
            mentionedUser = botFunctions.getName(message.from_user)
            text = mentionedUser + ' @ <b>' + message.chat.title + '</b> : ' + message.caption
            for userid in botFunctions.getAllUsers(message.chat.id):
                try:
                    bot.send_photo(chat_id=userid, photo=message.photo[-1].file_id, caption=text, parse_mode='HTML')
                except:
                    print('@all mention failed')

def mentionOnePhoto(bot, message):
    if (message.chat.type != 'private'):
        listUser = botFunctions.mentionedList(message.chat.id, message.caption)
        if (message.reply_to_message != None):
            if (message.reply_to_message.from_user.is_bot == False):
                if (botFunctions.isAvailable(message.chat.id, message.reply_to_message.from_user.id)):
                    try:
                        bot.send_message(chat_id=message.reply_to_message.from_user.id,
                                         text=botFunctions.getName(
                                             message.from_user) + ' @ <b>' + message.chat.title + '</b> : reply as a Photo',
                                         parse_mode='HTML')
                    except:
                        print('reply to photo failed')
                    listUser.append(str(message.reply_to_message.from_user.id))
                    listUser = list(set(listUser))
        if(len(listUser)>0):
            mentionedUser = botFunctions.getName(message.from_user)
            text = mentionedUser + ' @ <b>' + message.chat.title + '</b> : ' + message.caption
            for uname in listUser:
                try:
                    bot.send_photo(chat_id=uname, photo=message.photo[-1].file_id, caption=text, parse_mode='HTML')
                except:
                    print('single mention/subscribe failed')