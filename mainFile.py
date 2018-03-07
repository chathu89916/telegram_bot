# -*- coding: utf-8 -*-
import sys
sys.path.append('/mnt/c/Users/hp/AppData/Local/Programs/Python/Python36-32/Lib/site-packages')
import telebot
from telebot import types
import configuration
import common
import commandHandler
import textHandler
import stickerHandler
import newChatMemberHandler
import newChatTitleHandler
import migrateToChatIdHandler
import leftChatMemberHandler
import photoHandler
import videoHandler
import documentHandler
import audioHandler
import voiceHandler
import locationHandler
import contactHandler
import pinnedMessageHandler
import dbFunction

bot = telebot.TeleBot(configuration.botToken)
botID = configuration.botID
botUsername = configuration.botUsername

admin = configuration.admin

@bot.message_handler(commands=['start'])
def handle_command_botversion(message):
    commandHandler.start(bot, message)

@bot.message_handler(commands=['botversion'])
def handle_command_botversion(message):
    commandHandler.botVersion(bot, message)

@bot.message_handler(commands=['botlog'])
def handle_command_botversion(message):
    commandHandler.botLog(bot, message)

@bot.message_handler(commands=['addsuperadmin'])
def handle_command_botversion(message):
    if(message.from_user.id==admin and message.reply_to_message !=None):
        commandHandler.addSuperAdmin(bot, message)

@bot.message_handler(commands=['removesuperadmin'])
def handle_command_botversion(message):
    if(message.from_user.id==admin and message.reply_to_message !=None):
        commandHandler.removeSuperAdmin(bot, message)

@bot.message_handler(commands=['test'])
def handle_command_botversion(message):
    commandHandler.test(bot, message)

@bot.message_handler(commands=['all'])
def handle_command_botversion(message):
    commandHandler.all(bot, message)

@bot.message_handler(commands=['allusers'])
def handle_command_botversion(message):
    commandHandler.allusers(bot, message)

@bot.message_handler(commands=['allgroups'])
def handle_command_botversion(message):
    commandHandler.allgroups(bot, message)

@bot.message_handler(commands=['allgroupsadmins'])
def handle_command_botversion(message):
    commandHandler.allgroupsadmins(bot, message)

@bot.message_handler(commands=['allsuperadmins'])
def handle_command_botversion(message):
    commandHandler.allsuperadmins(bot, message)

@bot.message_handler(commands=['welcomemessage'])
def handle_command_botversion(message):
    commandHandler.welcomemessage(bot, message)

@bot.message_handler(commands=['stickerpermission'])
def handle_command_botversion(message):
    commandHandler.stickerpermission(bot, message)

@bot.message_handler(commands=['hhhpermission'])
def handle_command_botversion(message):
    commandHandler.hhhpermission(bot, message)

@bot.message_handler(commands=['subscribe'])
def handle_command_botversion(message):
    commandHandler.subscribe(bot, message)

@bot.message_handler(commands=['unsubscribe'])
def handle_command_botversion(message):
    commandHandler.unsubscribe(bot, message)

@bot.message_handler(commands=['subscribelist'])
def handle_command_botversion(message):
    commandHandler.subscribelist(bot, message)

@bot.message_handler(content_types=['new_chat_title'])
def handle_text(message):
    newChatTitleHandler.updateChatTitle(message)

@bot.message_handler(content_types=['migrate_to_chat_id'])
def handle_text(message):
    migrateToChatIdHandler.updateGroupID(message)

@bot.message_handler(content_types=['pinned_message'])
def handle_text(message):
    pinnedMessageHandler.pinnedPost(bot, message)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if (message.text.lower() == 'lal'):
        bot.send_message(chat_id=message.chat.id, text='සද දෙවිදු පිහිටයි!!!)')

    if (message.chat.type == 'private'):
        textHandler.privateText(bot, message)
        return

    common.autoAddDetails(message, bot, types)

    if (message.reply_to_message == None):
        if (dbFunction.getHHHPermission(message.chat.id)):
            textHandler.hhhFunc(bot, message)
    if (common.allCheck(message.text)):
        textHandler.mentionAll(bot, message)
        return

    textHandler.mentionOne(bot, message)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    if (message.chat.type == 'private'):
        photoHandler.privatePhoto(bot, message)
        return

    common.autoAddDetails(message, bot, types)

    if (message.reply_to_message == None):
        if(message.caption != None):
            if (common.allCheck(message.caption)):
                photoHandler.mentionAll(bot, message)
                return

    photoHandler.mentionOne(bot, message)

@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    if (message.chat.type == 'private'):
        audioHandler.privateAudio(bot, message)
        return

    common.autoAddDetails(message, bot, types)

    if (message.reply_to_message == None):
        if(message.caption != None):
            if (common.allCheck(message.caption)):
                videoHandler.mentionAll(bot, message)
                return

    audioHandler.mentionOne(bot, message)

@bot.message_handler(content_types=['video'])
def handle_video(message):
    if (message.chat.type == 'private'):
        videoHandler.privateVideo(bot, message)
        return

    common.autoAddDetails(message, bot, types)

    if (message.reply_to_message == None):
        if(message.caption != None):
            if (common.allCheck(message.caption)):
                videoHandler.mentionAll(bot, message)
                return

    videoHandler.mentionOne(bot, message)

@bot.message_handler(content_types=['document'])
def handle_document(message):
    if (message.chat.type == 'private'):
        documentHandler.privateDocument(bot, message)
        return

    common.autoAddDetails(message, bot, types)

    if (message.reply_to_message == None):
        if(message.caption != None):
            if (common.allCheck(message.caption)):
                documentHandler.mentionAll(bot, message)
                return

    documentHandler.mentionOne(bot, message)

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    if (message.chat.type == 'private'):
        voiceHandler.privateVoice(bot, message)
        return

    common.autoAddDetails(message, bot, types)

    if (message.reply_to_message == None):
        if(message.caption != None):
            if (common.allCheck(message.caption)):
                voiceHandler.mentionAll(bot, message)
                return

    voiceHandler.mentionOne(bot, message)

@bot.message_handler(content_types=['location'])
def handle_location(message):
    if (message.chat.type == 'private'):
        locationHandler.privateLocation(bot, message)
        return

    common.autoAddDetails(message, bot, types)

    if (message.reply_to_message != None):
        if (message.reply_to_message.from_user.id != botID):
            locationHandler.replyToLocation(bot, message, types)

@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    if (message.chat.type == 'private'):
        contactHandler.privateContact(bot, message)
        return

    common.autoAddDetails(message, bot, types)

    if (message.reply_to_message != None):
        if (message.reply_to_message.from_user.id != botID):
            contactHandler.replyToContact(bot, message, types)

@bot.message_handler(content_types=['sticker'])
def handle_stickers(message):
    if (message.chat.type == 'private'):
        stickerHandler.privateSticker(bot, message)
        return
    common.autoAddDetails(message, bot, types)
    stickerHandler.deleteSticker(bot, message)

@bot.message_handler(content_types=["new_chat_members", "group_chat_created"])
def handle_new_chat_member(message):
    if(message.content_type=='group_chat_created' or botID==message.new_chat_member.id):
        newChatMemberHandler.checkAndAdd(bot, message)
    else:
        newChatMemberHandler.welcomeToUser(bot, message)
        if(message.new_chat_member.is_bot == False):
            newChatMemberHandler.addingUser(bot, message, types)

@bot.message_handler(content_types=['left_chat_member'])
def handle_text(message):
    if(message.left_chat_member.id==botID):
        leftChatMemberHandler.kikBot(bot, message)
        return
    leftChatMemberHandler.leftMember(message)

@bot.callback_query_handler(func=lambda call: True)
def  test_callback(call):
    if (call.data == 'START'):
        bot.answer_callback_query(callback_query_id=call.id, url='https://telegram.me/'+str(botUsername)+'?start=XXXX')

bot.polling(none_stop=True, interval=0, timeout=0)