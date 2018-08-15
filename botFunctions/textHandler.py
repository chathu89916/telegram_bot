# -*- coding: utf-8 -*-
import configuration
import botFunctions
import re
from telebot import util

admin = configuration.admin

def privateText(bot, message):
    hhhFunc(bot, message)
    if(message.from_user.id == admin and message.reply_to_message != None):
        try:
            splitted_text = util.split_string(message.text, 3000)
            for text in splitted_text:
                bot.send_message(chat_id=message.reply_to_message.forward_from.id, text=text, parse_mode='HTML')
        except:
            print('Cannot send message to pm user')
        return
    if(message.from_user.id != admin):
        bot.forward_message(chat_id=admin, from_chat_id=message.chat.id, message_id=message.message_id)

def hhhFunc(bot, message):
    if(message.forward_from==None):
        if(message.text.lower() == 'hi'):
            try:
                bot.send_message(chat_id=message.chat.id, text='Hi ' + botFunctions.getName(message.from_user))
            except:
                bot.send_message(chat_id=admin, text='>>> exception found in hhhFunc')
            return
        if(message.text.lower() == 'hello'):
            try:
                bot.send_message(chat_id=message.chat.id, text='hello ' + botFunctions.getName(message.from_user))
            except:
                bot.send_message(chat_id=admin, text='>>> exception found in hhhFunc')
            return
        if(message.text.lower() == 'how are you' or message.text.lower() == 'how are you?'):
            try:
                bot.send_message(chat_id=message.chat.id, text='Im fine. How about you ' + botFunctions.getName(message.from_user))
            except:
                bot.send_message(chat_id=admin, text='>>> exception found in hhhFunc')
            return

def mentionAllText(bot, message):
    if (botFunctions.checkAdmin(bot, message.chat.id, message.from_user.id)):
        if(message.chat.type != 'private'):
            mentionedUser = botFunctions.getName(message.from_user)
            text = mentionedUser + ' @ <b>' + message.chat.title + '</b> : ' + message.text
            for userid in botFunctions.getAllUsers(message.chat.id):
                if (botFunctions.memberInTheGroup(bot, message.chat.id, userid)):
                    try:
                        splitted_text = util.split_string(text, 3000)
                        for text in splitted_text:
                            bot.send_message(chat_id=userid, text=text, parse_mode='HTML')
                    except:
                        print('@all mention failed')

def mentionOneText(bot, message):
    if (message.chat.type != 'private'):
        listUsers = botFunctions.mentionedList(message.chat.id, message.text)
        if (message.reply_to_message != None):
            if (message.reply_to_message.from_user.is_bot == False):
                if (botFunctions.isAvailable(message.chat.id, message.reply_to_message.from_user.id)):
                    listUsers.append(str(message.reply_to_message.from_user.id))
                    listUsers = list(set(listUsers))
        listSUB = re.split('\W+', message.text)
        listSUB = list(set(listSUB))
        if(len(listUsers)>0):
            mentionedUser = botFunctions.getName(message.from_user)
            for uname in listUsers:
                if (botFunctions.memberInTheGroup(bot, message.chat.id, uname)):
                    content = message.text
                    for subName in botFunctions.getSubscribeName(uname):
                        for sname in listSUB:
                            if(sname.lower()==subName.lower()):
                                botFunctions.updateSubscribeNameCount(sname, uname)
                                p = re.compile(r"\b{0}\b".format(sname))
                                content = p.sub("<b>" + sname + "</b>", content)
                    text = mentionedUser + ' @ <b>' + message.chat.title + '</b> : ' + content
                    try:
                        splitted_text = util.split_string(text, 3000)
                        for text in splitted_text:
                            bot.send_message(chat_id=uname, text=text, parse_mode='HTML')
                    except:
                        print('single mention/subscribe failed')