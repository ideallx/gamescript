# -*- coding: utf-8 -*-

from settings import *

class usercontrol:
    killed = 0
    saved = 0
    poisoned = 0
    couple1 = 0
    couple2 = 0
    guarded = 0
    
    userlist = []

    def __init__():
        for i in range(Settings.playerNum):
            usercontrol.userlist.append([0 for i in range(ArrayUser.TotalArraySize - 1)])

    def setUserRole(userid, roleid):
        usercontrol.userlist[userid][ArrayUser.Roles] = roleid

    def setUserLiveState(userid, ls):
        usercontrol.userlist[userid][ArrayUser.LiveState] = ls
        
    def setUserCamp(userid, camp):
        usercontrol.userlist[userid][ArrayUser.Camp] = camp

    def isWolf(userid):
        return usercontrol.userlist[userid][ArrayUser.Roles] == Rules.Wolves

    def morningCheck():
        return
