# -*- coding: utf-8 -*-
import sys
sys.path.append('/mnt/c/Users/hp/AppData/Local/Programs/Python/Python37-32/Lib/site-packages')
import telebot
from telebot import types
import configuration
import botFunctions
import emojiList

bot = telebot.TeleBot(configuration.botToken)
botID = configuration.botID
botUsername = configuration.botUsername

admin = configuration.admin

@bot.message_handler(commands=['adminwindow'])
def handle_command_adminwindow(message):
    botFunctions.adminWindowHandler(bot, types, message)

@bot.message_handler(commands=['start'])
def handle_command_start(message):
    botFunctions.start(bot, message)

@bot.message_handler(commands=['botversion'])
def handle_command_botversion(message):
    botFunctions.botVersion(bot, message)

@bot.message_handler(commands=['botlog'])
def handle_command_botlog(message):
    botFunctions.botLog(bot, message)

@bot.message_handler(commands=['addsuperadmin'])
def handle_command_addsuperadmin(message):
    if(message.from_user.id==admin and message.reply_to_message !=None):
        botFunctions.addSuperAdmin(bot, message)

@bot.message_handler(commands=['removesuperadmin'])
def handle_command_removesuperadmin(message):
    if(message.from_user.id==admin and message.reply_to_message !=None):
        botFunctions.removeSuperAdmin(bot, message)

@bot.message_handler(commands=['test'])
def handle_command_test(message):
    botFunctions.test(bot, message)

@bot.message_handler(commands=['all'])
def handle_command_all(message):
    botFunctions.all(bot, message)

@bot.message_handler(commands=['allusers'])
def handle_command_allusers(message):
    botFunctions.allusers(bot, message)

@bot.message_handler(commands=['allgroups'])
def handle_command_allgroups(message):
    botFunctions.allgroups(bot, message)

@bot.message_handler(commands=['allgroupsadmins'])
def handle_command_allgroupsadmins(message):
    botFunctions.allgroupsadmins(bot, message)

@bot.message_handler(commands=['allsuperadmins'])
def handle_command_allsuperadmins(message):
    botFunctions.allsuperadmins(bot, message)

@bot.message_handler(commands=['welcomemessage'])
def handle_command_welcomemessage(message):
    botFunctions.welcomemessage(bot, message)

@bot.message_handler(commands=['stickerpermission'])
def handle_command_stickerpermission(message):
    botFunctions.commandPermissionChange(bot, message, 'stickerPermission', 'Sticker Permission')

@bot.message_handler(commands=['hhhpermission'])
def handle_command_hhhpermission(message):
    botFunctions.commandPermissionChange(bot, message, 'hhhPermission', 'HHH Permission')

@bot.message_handler(commands=['audiopermission'])
def handle_command_hhhpermission(message):
    botFunctions.commandPermissionChange(bot, message, 'audioPermission', 'Audio Permission')

@bot.message_handler(commands=['videopermission'])
def handle_command_hhhpermission(message):
    botFunctions.commandPermissionChange(bot, message, 'videoPermission', 'Video Permission')

@bot.message_handler(commands=['documentpermission'])
def handle_command_hhhpermission(message):
    botFunctions.commandPermissionChange(bot, message, 'documentPermission', 'Document Permission')

@bot.message_handler(commands=['textpermission'])
def handle_command_hhhpermission(message):
    botFunctions.commandPermissionChange(bot, message, 'textPermission', 'Text Permission')

@bot.message_handler(commands=['locationpermission'])
def handle_command_hhhpermission(message):
    botFunctions.commandPermissionChange(bot, message, 'locationPermission', 'Location Permission')

@bot.message_handler(commands=['contactpermission'])
def handle_command_hhhpermission(message):
    botFunctions.commandPermissionChange(bot, message, 'contactPermission', 'Contact Permission')

@bot.message_handler(commands=['subscribe'])
def handle_command_subscribe(message):
    botFunctions.subscribe(bot, message)

# @bot.message_handler(commands=['unsubscribe'])
# def handle_command_unsubscribe(message):
#     botFunctions.unsubscribe(bot, message)

@bot.message_handler(commands=['subscribewindow'])
def handle_command_subscribewindow(message):
    botFunctions.subscribewindow(bot, types, message, False, "")

@bot.message_handler(content_types=['new_chat_title'])
def handle_new_chat_title(message):
    botFunctions.updateChatTitle(message)

@bot.message_handler(content_types=['migrate_to_chat_id'])
def handle_migrate_to_chat_id(message):
    botFunctions.updateGroupID(message)

@bot.message_handler(content_types=['pinned_message'])
def handle_pinned_message(message):
    botFunctions.pinnedPost(bot, message)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if (message.chat.type == 'private'):
        botFunctions.privateText(bot, message)
        return

    botFunctions.checkGroupStatus(bot, message)
    botFunctions.autoAddDetails(message, bot, types)

    if (message.reply_to_message == None):
        if (botFunctions.getHHHPermission(message.chat.id)):
            botFunctions.hhhFunc(bot, message)
    if (botFunctions.allCheck(message.text)):
        botFunctions.mentionAllText(bot, message)
        return

    botFunctions.mentionOneText(bot, message)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    if (message.chat.type == 'private'):
        botFunctions.privatePhoto(bot, message)
        return

    botFunctions.checkGroupStatus(bot, message)
    botFunctions.autoAddDetails(message, bot, types)

    if (message.reply_to_message == None):
        if(message.caption != None):
            if (botFunctions.allCheck(message.caption)):
                botFunctions.mentionAllPhoto(bot, message)
                return

    botFunctions.mentionOnePhoto(bot, message)

@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    if (message.chat.type == 'private'):
        botFunctions.privateAudio(bot, message)
        return

    botFunctions.checkGroupStatus(bot, message)
    botFunctions.autoAddDetails(message, bot, types)

    if (message.reply_to_message == None):
        if(message.caption != None):
            if (botFunctions.allCheck(message.caption)):
                botFunctions.mentionAllAudio(bot, message)
                return

    botFunctions.mentionOneAudio(bot, message)

@bot.message_handler(content_types=['video'])
def handle_video(message):
    if (message.chat.type == 'private'):
        botFunctions.privateVideo(bot, message)
        return

    botFunctions.checkGroupStatus(bot, message)
    botFunctions.autoAddDetails(message, bot, types)

    if (message.reply_to_message == None):
        if(message.caption != None):
            if (botFunctions.allCheck(message.caption)):
                botFunctions.mentionAllVideo(bot, message)
                return

    botFunctions.mentionOneVideo(bot, message)

@bot.message_handler(content_types=['document'])
def handle_document(message):
    if (message.chat.type == 'private'):
        botFunctions.privateDocument(bot, message)
        return

    botFunctions.checkGroupStatus(bot, message)
    botFunctions.autoAddDetails(message, bot, types)

    if (message.reply_to_message == None):
        if(message.caption != None):
            if (botFunctions.allCheck(message.caption)):
                botFunctions.mentionAllDocument(bot, message)
                return

    botFunctions.mentionOneDocument(bot, message)

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    if (message.chat.type == 'private'):
        botFunctions.privateVoice(bot, message)
        return

    botFunctions.checkGroupStatus(bot, message)
    botFunctions.autoAddDetails(message, bot, types)

    if (message.reply_to_message == None):
        if(message.caption != None):
            if (botFunctions.allCheck(message.caption)):
                botFunctions.mentionAllVoice(bot, message)
                return

    botFunctions.mentionOneVoice(bot, message)

@bot.message_handler(content_types=['location'])
def handle_location(message):
    if (message.chat.type == 'private'):
        botFunctions.privateLocation(bot, message)
        return

    botFunctions.checkGroupStatus(bot, message)
    botFunctions.autoAddDetails(message, bot, types)

    if (message.reply_to_message != None):
        if (message.reply_to_message.from_user.id != botID):
            botFunctions.replyToLocation(bot, message, types)

@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    if (message.chat.type == 'private'):
        botFunctions.privateContact(bot, message)
        return

    botFunctions.checkGroupStatus(bot, message)
    botFunctions.autoAddDetails(message, bot, types)

    if (message.reply_to_message != None):
        if (message.reply_to_message.from_user.id != botID):
            botFunctions.replyToContact(bot, message, types)

@bot.message_handler(content_types=['sticker'])
def handle_stickers(message):
    if (message.chat.type == 'private'):
        botFunctions.privateSticker(bot, message)
        return

    botFunctions.checkGroupStatus(bot, message)
    botFunctions.autoAddDetails(message, bot, types)
    botFunctions.deleteSticker(bot, message)

@bot.message_handler(content_types=["new_chat_members", "group_chat_created"])
def handle_new_chat_members_and_group_chat_created(message):
    if(message.content_type=='group_chat_created' or botID==message.new_chat_member.id):
        botFunctions.checkAndAdd(bot, message)
    else:
        botFunctions.welcomeToUser(bot, message, types)
        if(message.new_chat_member.is_bot == False):
            botFunctions.addingUser(bot, message, types)

@bot.message_handler(content_types=['left_chat_member'])
def handle_left_chat_member(message):
    if(message.left_chat_member.id==botID):
        botFunctions.kikBot(bot, message)
        return
    botFunctions.leftMember(message)

@bot.callback_query_handler(func=lambda call: True)
def  handle_query(call):
    if (call.data == 'START'):
        bot.answer_callback_query(callback_query_id=call.id, url="https://telegram.me/" + botUsername + "?start=XXXX")
    if(call.data == "superadmins"):
        botFunctions.superAdminHandler(bot, types, call, True)
    if (call.data == "groups"):
        botFunctions.groupHandler(bot, types, call, True)
    if (call.data == "allgroups"):
        botFunctions.allgroupsHandler(bot, types, call, True)
    if (call.data == "bannedgroups"):
        botFunctions.bannedGroupHandler(bot, types, call, True)
    if (call.data == "backToAllGroup"):
        botFunctions.allgroupsHandler(bot, types, call, True)
    if (call.data == 'noUserName'):
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="No Username Found " + emojiList.failFaceIcon)
    if (call.data == 'subscribenameNotification'):
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Click " + emojiList.crossIcon + " to remove the Subscribe Name")
    if (call.data == 'noGroupName'):
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Click " + emojiList.crossIcon + " to remove the Banned Group")
    if (call.data.startswith("['subscribename'")):
        botFunctions.unsubscribeFromWindow(bot, types, call)
    if (call.data == "backToHome"):
        botFunctions.adminWindow(bot, types, call.message, False)
    if (call.data.startswith("['superadmin'")):
        botFunctions.sureOrNot(bot, types, call)
    if (call.data.startswith("['removesuperadmin'")):
        botFunctions.removeSuperAdminQuery(bot, types, call)
    if (call.data.startswith("['group'")):
        botFunctions.sureOrNot(bot, types, call)
    if (call.data.startswith("['sureRemoveBannedGroup'")):
        botFunctions.sureOrNot(bot, types, call)
    if (call.data.startswith("['removegroup'")):
        botFunctions.removeGroup(bot, types, call)
    if (call.data.startswith("['viewgroup'")):
        botFunctions.viewGroupInfo(bot, types, call, '')
    if (call.data.startswith("['removeBannedGroup'")):
        botFunctions.removeBannedGroup(bot, types, call)
    if (call.data.startswith("['permission'")):
        botFunctions.displayPermissionStatus(bot, call)
    if (call.data.startswith("['cp'")):
        botFunctions.changePermissionStatus(bot, types, call)
    if (call.data == "no"):
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

bot.polling(none_stop=True, interval=0, timeout=0)