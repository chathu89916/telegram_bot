from botFunctions import *


def updateChatTitle(message):
    updateGroupTitle(message.chat.id, message.chat.title)
