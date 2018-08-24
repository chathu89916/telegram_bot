# -*- coding: utf-8 -*-
import configuration
import botFunctions

admin = configuration.admin


def privateContact(bot, message):
    if message.from_user.id == admin and message.reply_to_message is not None:
        try:
            if message.contact.last_name is not None:
                bot.send_contact(chat_id=message.reply_to_message.forward_from.id,
                                 phone_number=message.contact.phone_number, first_name=message.contact.first_name,
                                 last_name=message.contact.last_name)
            else:
                bot.send_contact(chat_id=message.reply_to_message.forward_from.id,
                                 phone_number=message.contact.phone_number, first_name=message.contact.first_name)
        except:
            print('Cannot send message to pm user')
        return
    if message.from_user.id != admin:
        bot.forward_message(chat_id=admin, from_chat_id=message.chat.id, message_id=message.message_id)


def replyToContact(bot, message, types):
    if botFunctions.isAvailable(message.chat.id, message.reply_to_message.from_user.id):
        try:
            bot.send_message(chat_id=message.reply_to_message.from_user.id,
                             text=botFunctions.getName(
                                 message.from_user) + ' @ <b>' + message.chat.title + '</b> : reply as a Contact',
                             parse_mode='HTML')
            if message.contact.last_name is not None:
                bot.send_contact(chat_id=message.reply_to_message.from_user.id,
                                 phone_number=message.contact.phone_number, first_name=message.contact.first_name,
                                 last_name=message.contact.last_name)
            else:
                bot.send_contact(chat_id=message.reply_to_message.from_user.id,
                                 phone_number=message.contact.phone_number, first_name=message.contact.first_name)
        except:
            botFunctions.exceptionHandling(message, bot, types, message.from_user)
