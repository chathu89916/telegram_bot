# -*- coding: utf-8 -*-
import configuration
from botFunctions import *
import re

admin = configuration.admin


def privatePhoto(bot, message):
    if message.from_user.id == admin and message.reply_to_message is not None:
        try:
            bot.send_photo(chat_id=message.reply_to_message.forward_from.id, photo=message.photo[-1].file_id,
                           caption=message.caption, parse_mode='HTML')
        except:
            print('Cannot send message to pm user')
        return
    if message.from_user.id != admin:
        bot.forward_message(chat_id=admin, from_chat_id=message.chat.id, message_id=message.message_id)


def mentionAllPhoto(bot, message):
    if checkAdmin(bot, message.chat.id, message.from_user.id):
        if message.chat.type != 'private':
            mentionedUser = getName(message.from_user)
            text = mentionedUser + ' @ <b>' + message.chat.title + '</b> : mention @all in a photo'
            for userid in getAllUsers(message.chat.id):
                if memberInTheGroup(bot, message.chat.id, userid):
                    try:
                        bot.send_message(chat_id=userid, text=text, parse_mode='HTML')
                        bot.send_photo(chat_id=userid, photo=message.photo[-1].file_id, caption=message.caption,
                                       parse_mode='HTML')
                    except:
                        print('@all mention failed')


def mentionOnePhoto(bot, message):
    if message.chat.type != 'private':
        listUser = []
        repliedUser = ''
        if message.caption is not None:
            listUser = mentionedList(message.chat.id, message.caption)
        if message.reply_to_message is not None:
            mentionedUser = getName(message.reply_to_message.from_user)
            if not message.reply_to_message.from_user.is_bot:
                if isAvailable(message.chat.id, message.reply_to_message.from_user.id):
                    if memberInTheGroup(bot, message.chat.id, message.reply_to_message.from_user.id):
                        repliedUser = message.reply_to_message.from_user.id
                        try:
                            bot.send_message(chat_id=repliedUser,
                                             text=getName(
                                                 message.from_user) + ' @ <b>' + message.chat.title + '</b> : reply as a Photo',
                                             parse_mode='HTML')
                        except:
                            print('reply to photo failed')
                        listUser.append(str(message.reply_to_message.from_user.id))
                        listUser = list(set(listUser))
                    else:
                        if str(message.reply_to_message.from_user.id) in listUser:
                            listUser.remove(str(message.reply_to_message.from_user.id))
        else:
            mentionedUser = getName(message.from_user)
        if len(listUser) > 0:
            for uname in listUser:
                if memberInTheGroup(bot, message.chat.id, uname):
                    text = None
                    if message.caption is not None:
                        text = message.caption
                        listSUB = re.split('\W+', message.caption)
                        listSUB = list(set(listSUB))
                        for subName in getSubscribeName(uname):
                            for sname in listSUB:
                                if sname.lower() == subName.lower():
                                    for i in range(text.count(sname)):
                                        updateSubscribeNameCount(sname, uname)
                                    p = re.compile(r"\b{0}\b".format(sname))
                                    text = p.sub("<b>" + sname + "</b>", text)
                    if str(repliedUser) != uname:
                        try:
                            bot.send_message(chat_id=uname,
                                             text=mentionedUser + ' @ <b>' + message.chat.title + '</b> : mention you in a photo',
                                             parse_mode='HTML')
                        except:
                            print("single mention/subscribe failed in photo")
                    try:
                        bot.send_photo(chat_id=uname, photo=message.photo[-1].file_id, caption=text, parse_mode='HTML')
                    except:
                        print('single mention/subscribe failed in photo')
