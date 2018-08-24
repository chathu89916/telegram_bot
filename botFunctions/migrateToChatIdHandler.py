from botFunctions import *


def updateGroupID(message):
    updateGroupIDDB(message.chat.id, message.migrate_to_chat_id)
