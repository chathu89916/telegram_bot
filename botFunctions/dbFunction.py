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
        c.execute("SELECT userid FROM users WHERE groupid='"+str(groupID)+"'")
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
        c.execute("SELECT u.userid FROM users u, allusers a WHERE a.userid=u.userid AND u.groupid='"+str(groupID)+"' AND a.uname='"+username+"'")
        for uID in c.fetchall():
            userID = uID[0]
    except Exception as e:
        userID = ''
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
        c.execute("INSERT INTO subscribe (subsname, userid, count) VALUES ('"+ subname +"', '"+ str(userID) +"', 0)")
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

def unsubscribeDB(subname, userID):
    status = ''
    try:
        conn, c = connectDB()
        c.execute("DELETE FROM subscribe WHERE userid='"+str(userID)+"' AND subsname='"+ subname+"'")
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
        c.execute("SELECT subsname FROM subscribe WHERE userid='"+str(userID)+"'")
        for row in c.fetchall():
            subscribersList.append(row[0])
    except Exception as e:
        subscribersList = []
        raise e
    finally:
        c.close()
        conn.close()
        return subscribersList

def updateSubscribeNameCount(subname, userID):
    try:
        conn, c = connectDB()
        c.execute("UPDATE subscribe SET count=count+1 WHERE userid='"+ str(userID) +"' AND subsname='"+ subname +"'")
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

def getSubscribeNameCount(subname, userID):
    wordCount = ''
    try:
        conn, c = connectDB()
        c.execute("SELECT count FROM subscribe WHERE userid='"+ str(userID) +"' AND subsname='"+ subname +"'")
        for welMsg in c.fetchall():
            wordCount = welMsg[0]
    except Exception as e:
        wordCount = ''
        raise e
    finally:
        c.close()
        conn.close()
        return wordCount

def getStickerPermission(groupID):
    stickerPermission = True
    try:
        conn, c = connectDB()
        c.execute("SELECT stickerPermission FROM groups WHERE groupid='"+ str(groupID) +"'")
        for permission in c.fetchall():
            stickerPermission = botFunctions.stringToBoolean(permission[0])
    except Exception as e:
        stickerPermission = True
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
        raise e
    finally:
        c.close()
        conn.close()
        return hhhPermission

def addToGroup(groupID, title):
    status = ''
    try:
        conn, c = connectDB()
        c.execute("INSERT INTO groups (groupid, title, welcomeMessage, stickerPermission, hhhPermission) VALUES ('"+ str(groupID) +"', '"+ title+"', 'Welcome #uname for <b>#title</b>', 'True', 'True')")
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
        c.execute("INSERT INTO users (groupid, userid) VALUES ('"+ str(groupID) +"', '"+ str(userID) +"')")
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
    firstName, lastName, userName = botFunctions.formatUserData(user)
    status = ''
    try:
        conn, c = connectDB()
        c.execute("INSERT INTO allusers (userid, fname, lname, uname) VALUES ('"+ str(user.id) +"', '"+ firstName +"', '"+ lastName +"', '"+ userName +"')")
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
    firstName, lastName, userName = botFunctions.formatUserData(user)
    status = ''
    try:
        conn, c = connectDB()
        c.execute("UPDATE allusers SET fname='"+ firstName +"', lname='"+ lastName +"', uname='"+ userName +"' WHERE userid='"+ str(user.id) +"'")
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
        c.execute("SELECT welcomeMessage FROM groups WHERE groupid='"+ str(groupID) +"'")
        for welMsg in c.fetchall():
            welcomeMessage = welMsg[0]
    except Exception as e:
        welcomeMessage = ''
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
        c.execute("UPDATE groups SET welcomeMessage='"+ msg +"' WHERE groupid='"+ str(groupID) +"'")
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
        c.execute("UPDATE groups SET title='" + title + "' WHERE groupid='" + str(groupID) + "'")
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

def getSubscribeUserCount():
    SubscribeUserCount = 0
    try:
        conn, c = connectDB()
        c.execute("SELECT COUNT(userid) FROM subscribe ")
        SubscribeUserCount = list(c.fetchone())[0]
    except Exception as e:
        SubscribeUserCount = 0
        raise e
    finally:
        c.close()
        conn.close()
        return SubscribeUserCount

def detailsOfSuperAdmins():
    bossArray = []
    try:
        conn, c = connectDB()
        c.execute('SELECT userid, fname, lname, uname FROM allusers WHERE userid IN (SELECT userid FROM superadmin)')
        for row in c.fetchall():
            bossArray.append(list(row))
    except Exception as e:
        bossArray = []
        raise e
    finally:
        c.close()
        conn.close()
        return bossArray

def detailsOfUser(userID):
    bossArray = []
    try:
        conn, c = connectDB()
        c.execute("SELECT userid, fname, lname, uname FROM allusers WHERE userid='"+str(userID)+"'")
        bossArray =list(c.fetchone())
    except Exception as e:
        bossArray = []
        raise e
    finally:
        c.close()
        conn.close()
        return bossArray

def detailsOfGroup(groupID):
    try:
        conn, c = connectDB()
        c.execute("SELECT title FROM groups WHERE groupid='"+str(groupID)+"'")
        groupTitle =c.fetchone()[0]
    except Exception as e:
        groupTitle = ''
        raise e
    finally:
        c.close()
        conn.close()
        return groupTitle

def removeFromGroup(groupID):
    status = False
    try:
        conn, c = connectDB()
        c.execute("DELETE FROM groups WHERE groupid='"+ str(groupID) +"'")
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