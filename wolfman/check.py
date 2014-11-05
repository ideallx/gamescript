# -*- coding: utf-8 -*- 

from rule import *
from settings import *
from usercontrol import *

class Check:
    def userNum(i):
        return i in range(Rules.MinUsers - 1, Rules.MaxUsers + 2)

    def setRole(i):
        if not Check.userNum(i):
            return False
        return Settings.rolelist[i] == 0

    def alive(i):
        if not Check.userNum(i):
            return False
        if guserlist[i] == 0:
            return False
        return Settings.userlist[i].live == LUndead

    def setCouple(i):
        if not Check.alive(i):
            return False

                                                                                                                                                                                                                                                                                                                                                                                                          
