# -*- coding: utf-8 -*-
import sys

sys.path.append('/mnt/c/Users/hp/AppData/Local/Programs/Python/Python37-32/Lib/site-packages')
import telebot
from telebot import types
import configuration
from botFunctions import *
import emojiList
import time

bot = telebot.TeleBot(configuration.botToken)
botID = configuration.botID
botUsername = configuration.botUsername

admin = configuration.admin


@bot.message_handler(commands=['adminwindow'])
def handle_command_adminwindow(message):
    adminWindowHandler(bot, types, message)


@bot.message_handler(commands=['start'])
def handle_command_start(message):
    start(bot, message)


@bot.message_handler(commands=['botversion'])
def handle_command_botversion(message):
    botVersion(bot, message)


@bot.message_handler(commands=['botlog'])
def handle_command_botlog(message):
    botLog(bot, message)


@bot.message_handler(commands=['addsuperadmin'])
def handle_command_addsuperadmin(message):
    if message.from_user.id == admin and message.reply_to_message is not None:
        addSuperAdmin(bot, message)


@bot.message_handler(commands=['removesuperadmin'])
def handle_command_removesuperadmin(message):
    if message.from_user.id == admin and message.reply_to_message is not None:
        removeSuperAdmin(bot, message)


@bot.message_handler(commands=['test'])
def handle_command_test(message):
    test(bot, message)


@bot.message_handler(commands=['all'])
def handle_command_all(message):
    all(bot, message)


@bot.message_handler(commands=['allusers'])
def handle_command_allusers(message):
    allusers(bot, message)


@bot.message_handler(commands=['allgroups'])
def handle_command_allgroups(message):
    allgroups(bot, message)


@bot.message_handler(commands=['allgroupsadmins'])
def handle_command_allgroupsadmins(message):
    allgroupsadmins(bot, message)


@bot.message_handler(commands=['allsuperadmins'])
def handle_command_allsuperadmins(message):
    allsuperadmins(bot, message)


@bot.message_handler(commands=['welcomemessage'])
def handle_command_welcomemessage(message):
    welcomemessage(bot, message)


@bot.message_handler(commands=['stickerpermission'])
def handle_command_stickerpermission(message):
    commandPermissionChange(bot, message, 'stickerPermission', 'Sticker Permission')


@bot.message_handler(commands=['hhhpermission'])
def handle_command_hhhpermission(message):
    commandPermissionChange(bot, message, 'hhhPermission', 'HHH Permission')


@bot.message_handler(commands=['audiopermission'])
def handle_command_audiopermission(message):
    commandPermissionChange(bot, message, 'audioPermission', 'Audio Permission')


@bot.message_handler(commands=['videopermission'])
def handle_command_videopermission(message):
    commandPermissionChange(bot, message, 'videoPermission', 'Video Permission')


@bot.message_handler(commands=['documentpermission'])
def handle_command_documentpermission(message):
    commandPermissionChange(bot, message, 'documentPermission', 'Document Permission')


@bot.message_handler(commands=['textpermission'])
def handle_command_textpermission(message):
    commandPermissionChange(bot, message, 'textPermission', 'Text Permission')


@bot.message_handler(commands=['locationpermission'])
def handle_command_locationpermission(message):
    commandPermissionChange(bot, message, 'locationPermission', 'Location Permission')


@bot.message_handler(commands=['contactpermission'])
def handle_command_contactpermission(message):
    commandPermissionChange(bot, message, 'contactPermission', 'Contact Permission')


@bot.message_handler(commands=['voicepermission'])
def handle_command_voicepermission(message):
    commandPermissionChange(bot, message, 'voicePermission', 'Voice Permission')


@bot.message_handler(commands=['photopermission'])
def handle_command_photopermission(message):
    commandPermissionChange(bot, message, 'photoPermission', 'Photo Permission')


@bot.message_handler(commands=['subscribe'])
def handle_command_subscribe(message):
    subscribe(bot, message)


# @bot.message_handler(commands=['unsubscribe'])
# def handle_command_unsubscribe(message):
#     unsubscribe(bot, message)

@bot.message_handler(commands=['subscribewindow'])
def handle_command_subscribewindow(message):
    subscribewindow(bot, types, message, False, "")


@bot.message_handler(content_types=['new_chat_title'])
def handle_new_chat_title(message):
    updateChatTitle(message)


@bot.message_handler(content_types=['migrate_to_chat_id'])
def handle_migrate_to_chat_id(message):
    updateGroupID(message)


@bot.message_handler(content_types=['pinned_message'])
def handle_pinned_message(message):
    pinnedPost(bot, message)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.chat.type == 'private':
        privateText(bot, message)
        return

    checkGroupStatus(bot, message)
    autoAddDetails(message, bot, types)
    deleteMessageAccordingToPermission(bot, message, 'textPermission', 'Text')

    if message.reply_to_message is None:
        if getStatusOfGroupPermission('hhhPermission', message.chat.id):
            hhhFunc(bot, message)
    if allCheck(message.text):
        mentionAllText(bot, message)
        return

    mentionOneText(bot, message)


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    if message.chat.type == 'private':
        privatePhoto(bot, message)
        return

    checkGroupStatus(bot, message)
    autoAddDetails(message, bot, types)
    deleteMessageAccordingToPermission(bot, message, 'photoPermission', 'Photo')

    if message.reply_to_message is None:
        if message.caption is not None:
            if allCheck(message.caption):
                mentionAllPhoto(bot, message)
                return

    mentionOnePhoto(bot, message)


@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    if message.chat.type == 'private':
        privateAudio(bot, message)
        return

    checkGroupStatus(bot, message)
    autoAddDetails(message, bot, types)
    deleteMessageAccordingToPermission(bot, message, 'audioPermission', 'Audio')

    if message.reply_to_message is None:
        if message.caption is not None:
            if allCheck(message.caption):
                mentionAllAudio(bot, message)
                return

    mentionOneAudio(bot, message)


@bot.message_handler(content_types=['video'])
def handle_video(message):
    if message.chat.type == 'private':
        privateVideo(bot, message)
        return

    checkGroupStatus(bot, message)
    autoAddDetails(message, bot, types)
    deleteMessageAccordingToPermission(bot, message, 'videoPermission', 'Video')

    if message.reply_to_message is None:
        if message.caption is not None:
            if allCheck(message.caption):
                mentionAllVideo(bot, message)
                return

    mentionOneVideo(bot, message)


@bot.message_handler(content_types=['document'])
def handle_document(message):
    if message.chat.type == 'private':
        privateDocument(bot, message)
        return

    checkGroupStatus(bot, message)
    autoAddDetails(message, bot, types)
    deleteMessageAccordingToPermission(bot, message, 'documentPermission', 'Document')

    if message.reply_to_message is None:
        if message.caption is not None:
            if allCheck(message.caption):
                mentionAllDocument(bot, message)
                return

    mentionOneDocument(bot, message)


@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    if message.chat.type == 'private':
        privateVoice(bot, message)
        return

    checkGroupStatus(bot, message)
    autoAddDetails(message, bot, types)
    deleteMessageAccordingToPermission(bot, message, 'voicePermission', 'Voice')

    if message.reply_to_message is None:
        if message.caption is not None:
            if allCheck(message.caption):
                mentionAllVoice(bot, message)
                return

    mentionOneVoice(bot, message)


@bot.message_handler(content_types=['location'])
def handle_location(message):
    if message.chat.type == 'private':
        privateLocation(bot, message)
        return

    checkGroupStatus(bot, message)
    autoAddDetails(message, bot, types)
    deleteMessageAccordingToPermission(bot, message, 'locationPermission', 'Location')

    if message.reply_to_message is not None:
        if message.reply_to_message.from_user.id != botID:
            replyToLocation(bot, message, types)


@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    if message.chat.type == 'private':
        privateContact(bot, message)
        return

    checkGroupStatus(bot, message)
    autoAddDetails(message, bot, types)
    deleteMessageAccordingToPermission(bot, message, 'contactPermission', 'Contact')

    if message.reply_to_message is not None:
        if (message.reply_to_message.from_user.id != botID):
            replyToContact(bot, message, types)


@bot.message_handler(content_types=['sticker'])
def handle_stickers(message):
    if message.chat.type == 'private':
        privateSticker(bot, message)
        return

    checkGroupStatus(bot, message)
    autoAddDetails(message, bot, types)
    deleteMessageAccordingToPermission(bot, message, 'stickerPermission', 'Stickers')

    if message.reply_to_message is not None:
        if message.reply_to_message.from_user.id != botID:
            replyToSticker(bot, message, types)


@bot.message_handler(content_types=["new_chat_members", "group_chat_created"])
def handle_new_chat_members_and_group_chat_created(message):
    if message.content_type == 'group_chat_created' or botID == message.new_chat_member.id:
        checkAndAdd(bot, message)
    else:
        welcomeToUser(bot, message, types)
        if not message.new_chat_member.is_bot:
            addingUser(bot, message, types)


@bot.message_handler(content_types=['left_chat_member'])
def handle_left_chat_member(message):
    if message.left_chat_member.id == botID:
        kikBot(bot, message)
        return
    leftMember(message)


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == 'START':
        bot.answer_callback_query(callback_query_id=call.id, url="https://telegram.me/" + botUsername + "?start=XXXX")
    if call.data == "superadmins":
        superAdminHandler(bot, types, call, True)
    if call.data == "groups":
        groupHandler(bot, types, call, True)
    if call.data == "allgroups":
        allgroupsHandler(bot, types, call, True)
    if call.data == "bannedgroups":
        bannedGroupHandler(bot, types, call, True)
    if call.data == "backToAllGroup":
        allgroupsHandler(bot, types, call, True)
    if call.data == 'noUserName':
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                  text="No Username Found " + emojiList.failFaceIcon)
    if call.data == 'subscribenameNotification':
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                  text="Click " + emojiList.crossIcon + " to remove the Subscribe Name")
    if call.data == 'noGroupName':
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                  text="Click " + emojiList.crossIcon + " to remove the Banned Group")
    if call.data.startswith("['subscribename'"):
        unsubscribeFromWindow(bot, types, call)
    if call.data == "backToHome":
        adminWindow(bot, types, call.message, False)
    if call.data.startswith("['superadmin'"):
        sureOrNot(bot, types, call)
    if call.data.startswith("['removesuperadmin'"):
        removeSuperAdminQuery(bot, types, call)
    if call.data.startswith("['group'"):
        sureOrNot(bot, types, call)
    if call.data.startswith("['sureRemoveBannedGroup'"):
        sureOrNot(bot, types, call)
    if call.data.startswith("['removegroup'"):
        removeGroup(bot, types, call)
    if call.data.startswith("['viewgroup'"):
        viewGroupInfo(bot, types, call, '')
    if call.data.startswith("['removeBannedGroup'"):
        removeBannedGroup(bot, types, call)
    if call.data.startswith("['permission'"):
        displayPermissionStatus(bot, call)
    if call.data.startswith("['cp'"):
        changePermissionStatus(bot, types, call)
    if call.data == "no":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=0)
    except:
        time.sleep(10)
