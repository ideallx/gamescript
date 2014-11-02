# -*- coding: utf-8 -*- 

from rule import *
from settings import *

class check:
    def userNum(i):
        return i in range(Rules.MinUsers, Rules.MaxUsers + 1)

    def setRole(i):
        if not checkUserNum(i):
            return False
        return guserlist[i] == 0

    def alive(i)
        if not checkUserNum(i):
            return False
        if guserlist[i] == 0:
            return False
        return guserlist[i].live == LUndead
                                                                                                                                                                                                                                                                                                                                                                                                          
