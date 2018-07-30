import botFunctions

def updateGroupID(message):
    botFunctions.updateGroupIDDB(message.chat.id, message.migrate_to_chat_id)