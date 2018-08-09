# -*- coding: utf-8 -*-
import configuration
import botFunctions

admin = configuration.admin

def privateDocument(bot, message):
    if(message.from_user.id == admin and message.reply_to_message != None):
        try:
            bot.send_document(chat_id=message.reply_to_message.forward_from.id, data=message.document.file_id, caption=message.caption, parse_mode='HTML')
        except:
            print('Cannot send message to pm user')
        return
    if(message.from_user.id != admin):
        bot.forward_message(chat_id=admin, from_chat_id=message.chat.id, message_id=message.message_id)

def mentionAllDocument(bot, message):
    if (botFunctions.checkAdmin(bot, message.chat.id, message.from_user.id)):
        if(message.chat.type != 'private'):
            mentionedUser = botFunctions.getName(message.from_user)
            text = mentionedUser + ' @ <b>' + message.chat.title + '</b> : ' + message.caption
            for userid in botFunctions.getAllUsers(message.chat.id):
                if (botFunctions.memberInTheGroup(bot, message.chat.id, userid)):
                    try:
                        bot.send_document(chat_id=userid, data=message.document.file_id, caption=text, parse_mode='HTML')
                    except:
                        print('@all mention failed')

def mentionOneDocument(bot, message):
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
                    bot.send_document(chat_id=uname, data=message.document.file_id, caption=text, parse_mode='HTML')
                except:
                    print('single mention/subscribe failed')