import botFunctions

def updateGroupID(message):
    botFunctions.updateGroupID(message.chat.id, message.migrate_to_chat_id)