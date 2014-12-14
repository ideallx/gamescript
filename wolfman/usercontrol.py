# -*- coding: utf-8 -*-

from settings import *

class User:
    role = Rules.Reserved
    camp = Camps.Undecided
    livestate = LiveStates.Undead

class usercontrol:
    killed = 0
    saved = 0
    poisoned = 0
    couple1 = 0
    couple2 = 0
    guarded = 0
    
    
    userlist = []

    def __init__():
        for i in range(Settings.playerNum + 1):
            usercontrol.userlist.append(User())

    def setUserRole(userid, roleid):
        usercontrol.userlist[userid].role = roleid

    def setUserLiveState(userid, ls):
        usercontrol.userlist[userid].livestate = ls
        
    def setUserCamp(userid, camp):
        usercontrol.userlist[userid].camp = camp

    def isWolf(userid):
        return usercontrol.userlist[userid].role == Rules.Wolves
    

    def morningCheck():
        return
