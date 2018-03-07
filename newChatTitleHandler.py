import dbFunction

def updateChatTitle(message):
    dbFunction.updateGroupTitle(message.chat.id, message.chat.title)