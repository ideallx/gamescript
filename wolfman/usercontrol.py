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
    userNum = [0 for i in range(Camps.TotalCamps)]

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

    def firstNightEnd():
        for i in range(1, Settings.playerNum + 1):
            if usercontrol.userlist[i].role == Rules.Reserved:
                usercontrol.userlist[i].role = Rules.Humen
                usercontrol.userlist[i].camp = Camps.Humen
                usercontrol.userNum[usercontrol.userlist[i].camp] += 1
        if usercontrol.couple1 != 0 and usercontrol.couple2 != 0:
            if usercontrol.userlist[usercontrol.couple1].role == Rules.Wolves ^ \
                    usercontrol.userlist[usercontrol.couple2].role == Rules.Wolves:
                usercontrol.userlist[usercontrol.couple1].camp = Camps.Wolfman
                usercontrol.userlist[usercontrol.couple2].camp = Camps.Wolfman

    def makeDeath(userid, reason, deathlist):
        deathlist.append(userid)
        usercontrol.userlist[userid].livestate = reason
        if userid == usercontrol.couple1:
            usercontrol.userlist[usercontrol.couple2].livestate = LiveStates.Couple
            deathlist.append(usercontrol.couple2)
        elif userid == usercontrol.couple2:
            usercontrol.userlist[usercontrol.couple1].livestate = LiveStates.Couple
            deathlist.append(usercontrol.couple1)

    def morningCheck():
        deathlist = []
        if usercontrol.killed != 0 and usercontrol.guarded != usercontrol.killed and \
                usercontrol.saved != usercontrol.killed:
            usercontrol.makeDeath(usercontrol.killed, LiveStates.Killed, deathlist)
        if usercontrol.poisoned != 0:
            usercontrol.makeDeath(usercontrol.poisoned, LiveStates.Poisoned, deathlist)

        usercontrol.killed = 0
        usercontrol.saved = 0
        usercontrol.poisoned = 0
        usercontrol.guarded = 0
        return deathlist

    def votekill(userid):
        deathlist = []
        usercontrol.makeDeath(userid, LiveStates.Voted, deathlist)
        return deathlist
