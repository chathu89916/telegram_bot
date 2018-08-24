# -*- coding: utf-8 -*-
import botFunctions


def pinnedPost(bot, message):
    mentionedUser = botFunctions.getName(message.from_user)
    text = mentionedUser + ' pinned a post @ <b>' + message.chat.title + '</b> : '
    for userid in botFunctions.getAllUsers(message.chat.id):
        if botFunctions.memberInTheGroup(bot, message.chat.id, userid):
            try:
                bot.send_message(chat_id=userid, text=text, parse_mode='HTML')
                bot.forward_message(chat_id=userid, from_chat_id=message.chat.id,
                                    message_id=message.pinned_message.message_id)
            except:
                print('@all mention failed')
