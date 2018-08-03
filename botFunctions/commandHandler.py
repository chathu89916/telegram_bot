# -*- coding: utf-8 -*-
import re
import configuration
import botFunctions

admin = configuration.admin

def subscribe(bot, message):
    userID = message.from_user.id
    subList = re.split('\W+', message.text, re.U)
    if(len(subList)==3):
        if(subList[2]!=''):
            subname = subList[2].lower()
            if(botFunctions.subscribeDB(userID, subname)=='success'):
                try:
                    bot.send_message(chat_id=userID, text='Subscribe name Successfully added')
                except:
                    print('Subscribe name successfully added failed')
            else:
                try:
                    bot.send_message(chat_id=userID, text='Subscribe name already there')
                except:
                    print('Subscribe name adding failed')
        else:
            try:
                bot.send_message(chat_id=userID, text='Subscribe name cannot be empty')
            except:
                print('Subscribe name cannot be empty')
    elif(len(subList)==2):
        try:
            bot.send_message(chat_id=userID, text='Please add a subscribe name')
        except:
            print('Subscriber name not found')
    else:
        try:
            bot.send_message(chat_id=userID, text='Cannot add more than one subscribe name same time')
        except:
            print('Cannot add more than one subscribe name same time')

def unsubscribe(bot, message):
    userID = message.from_user.id
    subList = re.split('\W+', message.text, re.U)
    if(len(subList)==3):
        if(subList[2]!=''):
            subname = subList[2].lower()
            subNameList = botFunctions.subscribelistDB(userID)
            for snm in subNameList:
                if(snm==subname):
                    if(botFunctions.unsubscribeDB(subname)=='success'):
                        try:
                            bot.send_message(chat_id=userID, text='Subscribe name Successfully Removed')
                        except:
                            print('Subscribe name successfully remove failed')
                    else:
                        try:
                            bot.send_message(chat_id=userID, text='Subscribe name Removing failed')
                        except:
                            print('Subscribe name removing failed')
                    return
            try:
                bot.send_message(chat_id=userID, text='Subscribe name cannot found')
            except:
                print('Subscribe name cannot found failed')
        else:
            try:
                bot.send_message(chat_id=userID, text='Unsubscribe name cannot be empty')
            except:
                print('Unsubscribe name cannot be empty')
    elif(len(subList)==2):
        try:
            bot.send_message(chat_id=userID, text='Please add a Unsubscribe name')
        except:
            print('Unsubscriber name not found')
    else:
        try:
            bot.send_message(chat_id=userID, text='Cannot remove more than one subscribe name same time')
        except:
            print('Cannot remove more than one subscribe name same time')

def subscribelist(bot, message):
    userID = message.from_user.id
    subList = botFunctions.subscribelistDB(userID)
    if(len(subList)!=0):
        txt = 'Here is your Subscribed Name List\n\n'
        for subname in subList:
            txt = txt + subname + "\n"
        try:
            bot.send_message(chat_id=userID, text=txt)
        except:
            print('Subscribe Name List sending failed')
    else:
        try:
            bot.send_message(chat_id=userID, text="Subscribed Name List is empty")
        except:
            print('Subscribe Name List sending failed')

def hhhpermission(bot, message):
    if (message.chat.type == 'private'):
        try:
            bot.send_message(chat_id=message.from_user.id, text="Please use this command inside the groups")
        except:
            print('hhhpermission private send failed')
    else:
        if (botFunctions.checkAdmin(bot, message.chat.id, message.from_user.id)):
            userID = message.from_user.id
            subList = re.split('\W+', message.text, re.U)
            if (len(subList) == 3):
                if (subList[2] != ''):
                    subname = subList[2].lower()
                    if(subname == "false"):
                        hhhpermission = False
                    elif(subname == "true"):
                        hhhpermission = True
                    else:
                        try:
                            bot.send_message(chat_id=userID, text='hhhpermission must be True or False')
                        except:
                            print('hhhpermission must be True or False')
                        return
                    if (botFunctions.updateHHHPermission(hhhpermission, message.chat.id) == 'success'):
                        try:
                            bot.send_message(chat_id=userID, text='hhh permission successfully changed')
                        except:
                            print('hhh permission successfully changed failed')
                    else:
                        try:
                            bot.send_message(chat_id=userID, text='hhh permission successfully changing failed')
                        except:
                            print('hhh permission successfully changing failed')
                else:
                    try:
                        bot.send_message(chat_id=userID, text='hhh permission cannot be empty')
                    except:
                        print('hhh permission cannot be empty')
            elif (len(subList) == 2):
                try:
                    bot.send_message(chat_id=userID, text='Please add a hhh permission')
                except:
                    print('hhh permission not found')
            else:
                try:
                    bot.send_message(chat_id=userID, text='Can add only one permission')
                except:
                    print('Cann add only one permission same time')

def stickerpermission(bot, message):
    if (message.chat.type == 'private'):
        try:
            bot.send_message(chat_id=message.from_user.id, text="Please use this command inside the groups")
        except:
            print('hhhpermission private send failed')
    else:
        if (botFunctions.checkAdmin(bot, message.chat.id, message.from_user.id)):
            userID = message.from_user.id
            subList = re.split('\W+', message.text, re.U)
            if (len(subList) == 3):
                if (subList[2] != ''):
                    subname = subList[2].lower()
                    if(subname == "false"):
                        hhhpermission = False
                    elif(subname == "true"):
                        hhhpermission = True
                    else:
                        try:
                            bot.send_message(chat_id=userID, text='Sticker Permission must be True or False')
                        except:
                            print('Sticker Permission must be True or False')
                        return
                    if (botFunctions.updateStickerPermission(hhhpermission, message.chat.id) == 'success'):
                        try:
                            bot.send_message(chat_id=userID, text='Sticker Permission successfully changed')
                        except:
                            print('Sticker Permission successfully changed failed')
                    else:
                        try:
                            bot.send_message(chat_id=userID, text='Sticker Permission successfully changing failed')
                        except:
                            print('Sticker Permission successfully changing failed')
                else:
                    try:
                        bot.send_message(chat_id=userID, text='Sticker Permission cannot be empty')
                    except:
                        print('Sticker Permission cannot be empty')
            elif (len(subList) == 2):
                try:
                    bot.send_message(chat_id=userID, text='Please add a Sticker Permission')
                except:
                    print('Sticker Permission not found')
            else:
                try:
                    bot.send_message(chat_id=userID, text='Can add only one permission')
                except:
                    print('Can add only one permission same time')

def welcomemessage(bot, message):
    if (message.chat.type == 'private'):
        try:
            bot.send_message(chat_id=message.from_user.id, text="Please use this command inside the groups")
        except:
            print('welcome message private send failed')
    else:
        if (botFunctions.checkAdmin(bot, message.chat.id, message.from_user.id)):
            userID = message.from_user.id
            subList = re.split(r'/welcomemessage\W', message.text, 1)
            if (len(subList) == 2):
                if (subList[1] != ''):
                    welcomeMessage = subList[1]
                    if (botFunctions.updateWelcomeMessage(welcomeMessage, message.chat.id) == 'success'):
                        try:
                            bot.send_message(chat_id=userID, text='Welcome Message successfully changed')
                        except:
                            print('Welcome Message successfully changed failed')
                    else:
                        try:
                            bot.send_message(chat_id=userID, text='Welcome Message successfully changing failed')
                        except:
                            print('Welcome Message successfully changing failed')
                else:
                    try:
                        bot.send_message(chat_id=userID, text='Welcome Message cannot be empty')
                    except:
                        print('Welcome Message cannot be empty')
            elif (len(subList) == 1):
                try:
                    bot.send_message(chat_id=userID, text='Please add a Valid Welcome Message')
                except:
                    print('valid welcome message failed')

def test(bot, message):
    if (botFunctions.isUserSuperAdmin(message.from_user.id)):
        if (message.chat.type != 'private'):
            try:
                bot.send_message(chat_id=message.from_user.id, text="Please use /test command in here")
            except:
                print('/test trying failed')
        else:
            userID = message.from_user.id
            subList = re.split(r'/test\W', message.text, 1)
            if (len(subList) == 2):
                if (subList[1] != ''):
                    allMessage = subList[1] + '\n\n/test by ' + botFunctions.getName(message.from_user)
                    try:
                        bot.send_message(chat_id=userID, text=allMessage, parse_mode='HTML')
                    except:
                        print("all message failed in sending")
                else:
                    try:
                        bot.send_message(chat_id=userID, text='All Message cannot be empty')
                    except:
                        print('All Message cannot be empty')
            elif (len(subList) == 1):
                try:
                    bot.send_message(chat_id=userID, text='Please add a Valid All Message')
                except:
                    print('valid All message failed')

def all(bot, message):
    if (botFunctions.isUserSuperAdmin(message.from_user.id)):
        if (message.chat.type != 'private'):
            try:
                bot.send_message(chat_id=message.from_user.id, text="Please use /all command in here")
            except:
                print('/all trying failed')
        else:
            userID = message.from_user.id
            subList = re.split(r'/all\W', message.text, 1)
            if (len(subList) == 2):
                if (subList[1] != ''):
                    allMessage = subList[1] + '\n\n/all by ' + botFunctions.getName(message.from_user)
                    for allID in botFunctions.allDB():
                        try:
                            bot.send_message(chat_id=allID, text=allMessage, parse_mode='HTML')
                        except:
                            print("all message failed in sending")
                else:
                    try:
                        bot.send_message(chat_id=userID, text='All Message cannot be empty')
                    except:
                        print('All Message cannot be empty')
            elif (len(subList) == 1):
                try:
                    bot.send_message(chat_id=userID, text='Please add a Valid All Message')
                except:
                    print('valid All message failed')

def allusers(bot, message):
    if (botFunctions.isUserSuperAdmin(message.from_user.id)):
        if (message.chat.type != 'private'):
            try:
                bot.send_message(chat_id=message.from_user.id, text="Please use /allusers command in here")
            except:
                print('/allusers trying failed')
        else:
            userID = message.from_user.id
            subList = re.split(r'/allusers\W', message.text, 1)
            if (len(subList) == 2):
                if (subList[1] != ''):
                    allMessage = subList[1] + '\n\n/allusers by ' + botFunctions.getName(message.from_user)
                    for allID in botFunctions.allusersDB():
                        try:
                            bot.send_message(chat_id=allID, text=allMessage, parse_mode='HTML')
                        except:
                            print("All Users message failed in sending")
                else:
                    try:
                        bot.send_message(chat_id=userID, text='All Users Message cannot be empty')
                    except:
                        print('All Users Message cannot be empty')
            elif (len(subList) == 1):
                try:
                    bot.send_message(chat_id=userID, text='Please add a Valid All Users Message')
                except:
                    print('valid All Users message failed')

def allgroups(bot, message):
    if (botFunctions.isUserSuperAdmin(message.from_user.id)):
        if (message.chat.type != 'private'):
            try:
                bot.send_message(chat_id=message.from_user.id, text="Please use /allgroups command in here")
            except:
                print('/allgroups trying failed')
        else:
            userID = message.from_user.id
            subList = re.split(r'/allgroups\W', message.text, 1)
            if (len(subList) == 2):
                if (subList[1] != ''):
                    allMessage = subList[1] + '\n\n/allgroups by ' + botFunctions.getName(message.from_user)
                    for allID in botFunctions.allgroupsDB():
                        try:
                            bot.send_message(chat_id=allID, text=allMessage, parse_mode='HTML')
                        except:
                            print("All Groups message failed in sending")
                else:
                    try:
                        bot.send_message(chat_id=userID, text='All Groups Message cannot be empty')
                    except:
                        print('All Groups Message cannot be empty')
            elif (len(subList) == 1):
                try:
                    bot.send_message(chat_id=userID, text='Please add a Valid All Groups Message')
                except:
                    print('valid All Groups message failed')

def allgroupsadmins(bot, message):
    if (botFunctions.isUserSuperAdmin(message.from_user.id)):
        if (message.chat.type != 'private'):
            try:
                bot.send_message(chat_id=message.from_user.id, text="Please use /allgroupsadmins command in here")
            except:
                print('/allgroupsadmins trying failed')
        else:
            adminList = []
            userID = message.from_user.id
            subList = re.split(r'/allgroupsadmins\W', message.text, 1)
            if (len(subList) == 2):
                if (subList[1] != ''):
                    allMessage = subList[1] + '\n\n/allgroupsadmins by ' + botFunctions.getName(message.from_user)
                    for allID in botFunctions.allgroupsDB():
                        try:
                            for admin in bot.get_chat_administrators(allID):
                                if (admin.user.is_bot == False):
                                    adminList.append(admin.user.id)
                        except:
                            print("Getdmins ID failed in  : " + str(allID))
                    adminList = list(set(adminList))
                    for adminID in adminList:
                        try:
                            bot.send_message(chat_id=adminID, text=allMessage, parse_mode='HTML')
                        except:
                            print("All Groups Admin message failed in sending")
                else:
                    try:
                        bot.send_message(chat_id=userID, text='All Groups Admin Message cannot be empty')
                    except:
                        print('All Groups Admin Message cannot be empty')
            elif (len(subList) == 1):
                try:
                    bot.send_message(chat_id=userID, text='Please add a Valid All Groups Admin Message')
                except:
                    print('valid All Groups Admin message failed')

def allsuperadmins(bot, message):
    if (message.from_user.id==configuration.admin):
        if (message.chat.type != 'private'):
            try:
                bot.send_message(chat_id=message.from_user.id, text="Please use /allsuperadmins command in here")
            except:
                print('/allsuperadmins trying failed')
        else:
            userID = message.from_user.id
            subList = re.split(r'/allsuperadmins\W', message.text, 1)
            if (len(subList) == 2):
                if (subList[1] != ''):
                    allMessage = subList[1] + '\n\n/allsuperadmins by ' + botFunctions.getName(message.from_user)
                    for allID in botFunctions.getAdmin():
                        try:
                            bot.send_message(chat_id=allID, text=allMessage, parse_mode='HTML')
                        except:
                            print("All Groups Super Admin message failed in sending")
                else:
                    try:
                        bot.send_message(chat_id=userID, text='All Groups Super Admin Message cannot be empty')
                    except:
                        print('All Groups Super Admin Message cannot be empty')
            elif (len(subList) == 1):
                try:
                    bot.send_message(chat_id=userID, text='Please add a Valid All Groups Super Admin Message')
                except:
                    print('valid All Groups Super Admin message failed')

def start(bot, message):
    if (botFunctions.addToAllUser(message.from_user) == 'failed'):
        if (botFunctions.updateToAllUser(message.from_user) == 'failed'):
            try:
                bot.send_message(chat_id=message.from_user.id, text='Cannot update your details ' + botFunctions.getName(message.from_user))
            except:
                print('User update failed')
                bot.send_message(chat_id=admin, text='Cannot update details for ' + botFunctions.getName(message.from_user))
        else:
            try:
                bot.send_message(chat_id=message.from_user.id, text='You Already STARTed me ' + botFunctions.getName(message.from_user) + ' and updated your personal details')
            except:
                print('User update failed')
    else:
        try:
            bot.send_message(chat_id=admin, text='Bot started for ' + botFunctions.getName(message.from_user))
            bot.send_message(chat_id=message.from_user.id, text='Thank you for STARTing me ' + botFunctions.getName(message.from_user))
        except:
            print('User start failed')

def addSuperAdmin(bot, message):
    if(message.reply_to_message.from_user.is_bot==False):
        if(botFunctions.addToSuperAdmin(message.reply_to_message.from_user.id)):
            bot.send_message(chat_id=admin, text='Successfully added ' + botFunctions.getName(message.reply_to_message.from_user) +' as a Super Admin')
        else:
            bot.send_message(chat_id=admin, text='Failed to add ' + botFunctions.getName(message.reply_to_message.from_user) +' as a Super Admin')

def removeSuperAdmin(bot, message):
    if(message.reply_to_message.from_user.is_bot==False):
        if(botFunctions.removeFromSuperAdmin(message.reply_to_message.from_user.id)):
            bot.send_message(chat_id=admin, text='Successfully removed ' + botFunctions.getName(message.reply_to_message.from_user) +' from Super Admin')
        else:
            bot.send_message(chat_id=admin, text='Failed to remove ' + botFunctions.getName(message.reply_to_message.from_user) +' from Super Admin')

def botVersion(bot, message):
    try:
        bot.send_message(chat_id=message.chat.id, text=botFunctions.botVesion(), parse_mode='HTML')
    except:
        print('botVersion seding failed')

def botLog(bot, message):
    try:
        bot.send_message(chat_id=message.chat.id, text=botFunctions.changeLOG(), parse_mode='HTML')
    except:
        print('botLog seding failed')

def adminWindow(bot, types, message):
    usersIcon = u"\U0001F465"
    houseIcon = u"\U0001F3E1"
    subscribeUserIcon = u"\U0001F5E3"
    allUserCount = botFunctions.allusersDB().__len__()
    allGroupCount = botFunctions.allgroupsDB().__len__()
    subscribeUserCount = botFunctions.getSubscribeUserCount()
    firstMessage = """<b>Admin Window</b>
    
"""+usersIcon+""" All Users : """+str(allUserCount)+"""
"""+houseIcon+""" All Groups : """+str(allGroupCount)+"""
"""+subscribeUserIcon+""" Subscribe Names : """+str(subscribeUserCount)+"""
"""
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Super Admins", callback_data="superadmins"), types.InlineKeyboardButton("Groups", callback_data="groups"))
    bot.send_message(chat_id=message.chat.id, text=firstMessage, reply_markup=markup, parse_mode='HTML')
