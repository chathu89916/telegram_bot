# -*- coding: utf-8 -*-
import sqlite3
import botFunctions
import configuration

dbName = configuration.dbName

def connectDB():
    conn = sqlite3.connect(dbName, check_same_thread=False)
    c = conn.cursor()
    return conn, c

def getAllUsers(groupID):
    usersArray = []
    try:
        conn, c = connectDB()
        c.execute('SELECT userid FROM users WHERE groupid='+str(groupID))
        for row in c.fetchall():
            usersArray.append(row[0])
    except Exception as e:
        usersArray = []
        raise e
    finally:
        c.close()
        conn.close()
        return usersArray

def getAdmin():
    bossArray = []
    try:
        conn, c = connectDB()
        c.execute('SELECT userid FROM superadmin')
        for row in c.fetchall():
            bossArray.append(row[0])
    except Exception as e:
        bossArray = []
        raise e
    finally:
        c.close()
        conn.close()
        return bossArray

def getMentionedUser(groupID, username):
    userID = ''
    try:
        conn, c = connectDB()
        c.execute("SELECT u.userid FROM users u, allusers a WHERE a.userid=u.userid AND u.groupid='"+str(groupID)+"' AND a.uname='"+str(username)+"'")
        for uID in c.fetchall():
            userID = uID[0]
    except Exception as e:
        userID = ''
        conn.rollback()
        raise e
    finally:
        c.close()
        conn.close()
        return userID

def getSubscribeUser(subName):
    userID = []
    try:
        conn, c = connectDB()
        c.execute("SELECT userid FROM subscribe WHERE subsname='"+subName+"'")
        for uID in c.fetchall():
            userID.append(uID[0])
    except Exception as e:
        userID = []
        conn.rollback()
        raise e
    finally:
        c.close()
        conn.close()
        return userID

def getSubscribeName(userID):
    subscribersArray = []
    try:
        conn, c = connectDB()
        c.execute("SELECT subsname FROM subscribe WHERE userid='"+str(userID)+"'")
        for row in c.fetchall():
            subscribersArray.append(row[0])
    except Exception as e:
        subscribersArray = []
        raise e
    finally:
        c.close()
        conn.close()
        return subscribersArray

def isAvailable(groupID, useID):
    userID = ''
    try:
        conn, c = connectDB()
        c.execute("SELECT userid FROM users WHERE groupid='" + str(groupID) + "' AND userid='" + str(useID) + "'")
        for uID in c.fetchall():
            userID = uID[0]
    except Exception as e:
        userID = ''
        conn.rollback()
        raise e
    finally:
        c.close()
        conn.close()
        if(userID==''):
            return False
        else:
            return True

def subscribeDB(userID, subname):
    status = ''
    try:
        conn, c = connectDB()
        c.execute("INSERT INTO subscribe (subsname, userid) VALUES ('"+ subname +"', '"+ str(userID)+"')")
        conn.commit()
        status = 'success'
    except Exception as e:
        status = 'failed'
        conn.rollback()
        raise e
    finally:
        c.close()
        conn.close()
        return status

def unsubscribeDB(subname):
    status = ''
    try:
        conn, c = connectDB()
        c.execute("DELETE FROM subscribe WHERE subsname='"+ str(subname)+"'")
        conn.commit()
        status = 'success'
    except Exception as e:
        status = 'failed'
        conn.rollback()
        raise e
    finally:
        c.close()
        conn.close()
        return status

def subscribelistDB(userID):
    subscribersList = []
    try:
        conn, c = connectDB()
        c.execute('SELECT subsname FROM subscribe WHERE userid='+str(userID))
        for row in c.fetchall():
            subscribersList.append(row[0])
    except Exception as e:
        subscribersList = []
        raise e
    finally:
        c.close()
        conn.close()
        return subscribersList

def getStickerPermission(groupID):
    stickerPermission = True
    try:
        conn, c = connectDB()
        c.execute("SELECT stickerPermission FROM groups WHERE groupid='"+ str(groupID) +"'")
        for permission in c.fetchall():
            stickerPermission = botFunctions.stringToBoolean(permission[0])
    except Exception as e:
        stickerPermission = True
        conn.rollback()
        raise e
    finally:
        c.close()
        conn.close()
        return stickerPermission

def getHHHPermission(groupID):
    hhhPermission = True
    try:
        conn, c = connectDB()
        c.execute("SELECT hhhPermission FROM groups WHERE groupid='"+ str(groupID) +"'")
        for permission in c.fetchall():
            hhhPermission = botFunctions.stringToBoolean(permission[0])
    except Exception as e:
        hhhPermission = True
        conn.rollback()
        raise e
    finally:
        c.close()
        conn.close()
        return hhhPermission

def addToGroup(groupID, title):
    status = ''
    try:
        conn, c = connectDB()
        c.execute("INSERT INTO groups (groupid, title, welcomeMessage, stickerPermission, hhhPermission) VALUES ('"+ str(groupID) +"', '"+ str(title)+"', 'Welcome #uname for #title', 'True', 'True')")
        conn.commit()
        status = 'success'
    except Exception as e:
        status = 'failed'
        conn.rollback()
        raise e
    finally:
        c.close()
        conn.close()
        return status

def addToUser(groupID, userID):
    status = ''
    try:
        conn, c = connectDB()
        c.execute("INSERT INTO users (groupid, userid) VALUES ('"+ str(groupID) +"', '"+ str(userID)+"')")
        conn.commit()
        status = 'success'
    except Exception as e:
        status = 'failed'
        conn.rollback()
        raise e
    finally:
        c.close()
        conn.close()
        return status

def addToAllUser(user):
    status = ''
    try:
        conn, c = connectDB()
        c.execute("INSERT INTO allusers (userid, fname, lname, uname) VALUES ('"+ str(user.id) +"', '"+ str(user.first_name)+"', '"+ str(user.last_name) +"', '"+ str(user.username.lower()) +"')")
        conn.commit()
        status = 'success'
    except Exception as e:
        status = 'failed'
        conn.rollback()
        raise e
    finally:
        c.close()
        conn.close()
        return status

def updateToAllUser(user):
    status = ''
    try:
        conn, c = connectDB()
        c.execute("UPDATE allusers SET fname='"+ str(user.first_name) +"', lname='"+ str(user.last_name) +"', uname='"+ str(user.username.lower()) +"' WHERE userid='"+ str(user.id) +"'")
        conn.commit()
        status = 'success'
    except Exception as e:
        status = 'failed'
        conn.rollback()
        raise e
    finally:
        c.close()
        conn.close()
        return status

def getWelcomeMessage(groupID):
    welcomeMessage = ''
    try:
        conn, c = connectDB()
        c.execute("SELECT welcomeMessage FROM groups WHERE groupid='"+str(groupID)+"'")
        for welMsg in c.fetchall():
            welcomeMessage = welMsg[0]
    except Exception as e:
        welcomeMessage = ''
        conn.rollback()
        raise e
    finally:
        c.close()
        conn.close()
        return welcomeMessage

def updateHHHPermission(permission, groupID):
    status = ''
    try:
        conn, c = connectDB()
        c.execute("UPDATE groups SET hhhPermission='"+ str(permission) +"' WHERE groupid='"+ str(groupID) +"'")
        conn.commit()
        status = 'success'
    except Exception as e:
        status = 'failed'
        conn.rollback()
        raise e
    finally:
        c.close()
        conn.close()
        return status

def updateStickerPermission(permission, groupID):
    status = ''
    try:
        conn, c = connectDB()
        c.execute("UPDATE groups SET stickerPermission='"+ str(permission) +"' WHERE groupid='"+ str(groupID) +"'")
        conn.commit()
        status = 'success'
    except Exception as e:
        status = 'failed'
        conn.rollback()
        raise e
    finally:
        c.close()
        conn.close()
        return status

def updateWelcomeMessage(msg, groupID):
    try:
        conn, c = connectDB()
        c.execute("UPDATE groups SET welcomeMessage='"+ str(msg) +"' WHERE groupid='"+ str(groupID) +"'")
        conn.commit()
        status = 'success'
    except Exception as e:
        status = 'failed'
        conn.rollback()
        print(e)
        raise e
    finally:
        c.close()
        conn.close()
        return status

def allusersDB():
    usersArray = []
    try:
        conn, c = connectDB()
        c.execute("SELECT userid FROM allusers")
        for row in c.fetchall():
            usersArray.append(row[0])
    except Exception as e:
        usersArray = []
        raise e
    finally:
        c.close()
        conn.close()
        return usersArray

def allgroupsDB():
    groupsArray = []
    try:
        conn, c = connectDB()
        c.execute("SELECT groupid FROM groups")
        for row in c.fetchall():
            groupsArray.append(row[0])
    except Exception as e:
        groupsArray = []
        raise e
    finally:
        c.close()
        conn.close()
        return groupsArray

def allDB():
    all = []
    for userID in allusersDB():
        all.append(userID)
    for groupID in allgroupsDB():
        all.append(groupID)
    return all

def getGroupIDTitle():
    groupsArray = []
    try:
        conn, c = connectDB()
        c.execute("SELECT groupid,title FROM groups")
        for row in c.fetchall():
            print(row)
            groupsArray.append(row)
    except Exception as e:
        groupsArray = []
        raise e
    finally:
        c.close()
        conn.close()
        return groupsArray

def updateGroupIDDB(oldID, newID):
    status = ''
    try:
        conn, c = connectDB()
        c.execute("UPDATE groups SET groupid='"+ str(newID) +"' WHERE groupid='"+ str(oldID) +"'")
        c.execute("UPDATE users SET groupid='" + str(newID) + "' WHERE groupid='" + str(oldID) + "'")
        conn.commit()
        status = 'success'
    except Exception as e:
        status = 'failed'
        conn.rollback()
        raise e
    finally:
        c.close()
        conn.close()
        return status

def updateGroupTitle(groupID, title):
    status = ''
    try:
        conn, c = connectDB()
        c.execute("UPDATE groups SET title='" + str(title) + "' WHERE groupid='" + str(groupID) + "'")
        conn.commit()
        status = 'success'
    except Exception as e:
        status = 'failed'
        conn.rollback()
        raise e
    finally:
        c.close()
        conn.close()
        return status

def leftOfKikMember(groupID, userID):
    status = ''
    try:
        conn, c = connectDB()
        c.execute("DELETE FROM users WHERE groupid='"+ str(groupID) +"' AND userid='"+ str(userID) +"'")
        conn.commit()
        status = 'success'
    except Exception as e:
        status = 'failed'
        conn.rollback()
        raise e
    finally:
        c.close()
        conn.close()
        return status

def kikBotDB(groupID):
    status = ''
    try:
        conn, c = connectDB()
        c.execute("DELETE FROM groups WHERE groupid='" + str(groupID) + "'")
        c.execute("DELETE FROM users WHERE groupid='"+ str(groupID) +"'")
        conn.commit()
        status = 'success'
    except Exception as e:
        status = 'failed'
        conn.rollback()
        raise e
    finally:
        c.close()
        conn.close()
        return status

def addToSuperAdmin(userID):
    status = False
    try:
        conn, c = connectDB()
        c.execute("INSERT INTO superadmin (userid) VALUES ('"+ str(userID) +"')")
        conn.commit()
        status = True
    except Exception as e:
        status = False
        conn.rollback()
        raise e
    finally:
        c.close()
        conn.close()
        return status

def removeFromSuperAdmin(userID):
    status = False
    try:
        conn, c = connectDB()
        c.execute("DELETE FROM superadmin WHERE userid='"+ str(userID) +"'")
        conn.commit()
        status = True
    except Exception as e:
        status = False
        conn.rollback()
        raise e
    finally:
        c.close()
        conn.close()
        return status