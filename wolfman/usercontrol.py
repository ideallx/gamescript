# -*- coding: utf-8 -*-

from gamerole import *
from role import *

class usercontrol:
    killed = 0
    couple1 = 0
    couple2 = 0

    def __init__(self):
        self.killed = 0
        self.couple1 = 0
        self.couple2 = 0

    def coupledeathcheck(self, u1):
        if u1 == self.couple1:
            return self.couple2
        elif u1 == self.couple2:
            return self.couple1
        else:
            return 0

    def setremindasnormal(self):
        for i in range(1, self.gamerole.numtotal + 1):
            if guserlist[i] == 0:
                setuser(i, RHumen)

    def dayoff(self):
        if self.guardeduser == self.killed:
            self.killed = 0

        if self.saveduser == self.killed:
            self.killed = 0

        result = []
        if not self.killed == 0:
            result.append(self.killed)
            self.death(self.killed, "狼人咬死")
            
        if not self.poisoneduser == 0:
            result.append(self.poisoneduser)
            self.death(self.poisoneduser, "女巫毒死")

        couple = 0
        for i in result:
            couple = self.coupledeathcheck(i)
            if not couple == 0:
                break

        if not couple == 0:
            result.append(couple)
            self.death(couple, "情侣带死")

        self.guardeduser = 0
        if self.ispoisoned == True:
            self.poisoneduser = 0
        if self.issaved == True:
            self.saveduser = 0
            
        self.printuserstate()
        return result

    def wolfkill(self, u1):
        if u1 == 0:
            return
        self.killed = u1

    def guard(self, u1):
        if u1 == self.lastguard or u1 == 0:
            return False
        self.lastguard = self.guardeduser = u1
        return True

    def witchsave(self):
        if self.issaved or self.killed == 0:
            return

        self.issaved = True
        self.saveduser = self.killed

    def witchpoison(self, u1):
        if self.ispoisoned or u1 == 0:
            return

        self.ispoisoned = True
        self.poisoneduser = u1

    def iswolf(self, u1):
        if self.userlist[u1][2] == "狼人":
            return True
        else:
            return False

    def votekill(self, u1):
        if u1 == 0:
            return
        self.death(u1, "选票票死")
        
        

