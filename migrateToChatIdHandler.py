import dbFunction

def updateGroupID(message):
    dbFunction.updateGroupID(message.chat.id, message.migrate_to_chat_id)