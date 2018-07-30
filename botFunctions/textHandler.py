# -*- coding: utf-8 -*-
import configuration
import common
import botFunctions
import re

admin = configuration.admin

def privateText(bot, message):
    hhhFunc(bot, message)
    if(message.from_user.id == admin and message.reply_to_message != None):
        try:
            bot.send_message(chat_id=message.reply_to_message.forward_from.id, text=message.text, parse_mode='HTML')
        except:
            print('Cannot send message to pm user')
        return
    if(message.from_user.id != admin):
        bot.forward_message(chat_id=admin, from_chat_id=message.chat.id, message_id=message.message_id)

def hhhFunc(bot, message):
    if(message.text.lower() == 'hi'):
        try:
            bot.send_message(chat_id=message.chat.id, text='Hi ' + common.getName(message.from_user))
        except:
            bot.send_message(chat_id=admin, text='>>> exception found in hhhFunc')
        return
    if(message.text.lower() == 'hello'):
        try:
            bot.send_message(chat_id=message.chat.id, text='hello ' + common.getName(message.from_user))
        except:
            bot.send_message(chat_id=admin, text='>>> exception found in hhhFunc')
        return
    if(message.text.lower() == 'how are you' or message.text.lower() == 'how are you?'):
        try:
            bot.send_message(chat_id=message.chat.id, text='Im fine. How about you ' + common.getName(message.from_user))
        except:
            bot.send_message(chat_id=admin, text='>>> exception found in hhhFunc')
        return

def mentionAll(bot, message):
    if (common.checkAdmin(bot, message.chat.id, message.from_user.id)):
        if(message.chat.type != 'private'):
            mentionedUser = common.getName(message.from_user)
            text = mentionedUser + ' @ <b>' + message.chat.title + '</b> : ' + message.text
            for userid in botFunctions.getAllUsers(message.chat.id):
                try:
                    bot.send_message(chat_id=userid, text=text, parse_mode='HTML')
                except:
                    print('@all mention failed')

def mentionOne(bot, message):
    if (message.chat.type != 'private'):
        listUsers = common.mentionedList(message.chat.id, message.text)
        if (message.reply_to_message != None):
            if (message.reply_to_message.from_user.is_bot == False):
                if (botFunctions.isAvailable(message.chat.id, message.reply_to_message.from_user.id)):
                    listUsers.append(str(message.reply_to_message.from_user.id))
                    listUsers = list(set(listUsers))
        listSUB = re.split('\W+', message.text)
        listSUB = list(set(listSUB))
        if(len(listUsers)>0):
            mentionedUser = common.getName(message.from_user)
            for uname in listUsers:
                content = message.text
                for subName in botFunctions.getSubscribeName(uname):
                    for sname in listSUB:
                        if(sname.lower()==subName.lower()):
                            p = re.compile('(' + str(sname) + ')')
                            content = p.sub("<b>" + str(sname) + "</b>", content)
                text = mentionedUser + ' @ <b>' + message.chat.title + '</b> : ' + content
                try:
                    bot.send_message(chat_id=uname, text=text, parse_mode='HTML')
                except:
                    print('single mention/subscribe failed')