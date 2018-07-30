import botFunctions

def updateChatTitle(message):
    botFunctions.updateGroupTitle(message.chat.id, message.chat.title)