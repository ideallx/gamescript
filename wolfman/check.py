# -*- coding: utf-8 -*- 

from rule import *
from settings import *
from usercontrol import *

class Check:
    def userNum(i):
        return i in range(Rules.MinUsers, Rules.MaxUsers)

    def userSeq(i):
        return i in range(Settings.playerNum + 1)

    def setRole(i):
        if not Check.userSeq(i):
            return False
        return usercontrol.userlist[i].role == Rules.Reserved

    def alive(i):
        if not Check.userSeq(i):
            return False
        return usercontrol.userlist[i].livestate == LiveStates.Undead

    def setCouple(i):
        if not Check.userSeq(i):
            return False

        if not Check.alive(i):
            return False

        return True
