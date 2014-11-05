# -*- coding: utf-8 -*- 

from role import *
from check import *

def actfirstnight(roleid):
    role = Roles.getRole(roleid)
    if role == 0:
        return

    role.fnact()
    role.nact()
    role.anact()

def actnight(roleid):
    role = Roles.getRole(roleid)
    if role == 0:
        return
    role.nact()
    role.anact()
    
class wolfman:
    def __init__(self):
        Settings.playerNum = Ask.playerNums(Check.userNum)

    def firstnight(self):
        GodSays.closeEyeAll()

        for i in range(len(Rules.Morning)):
            actfirstnight(Rules.Morning[i])
#        self.uc.setremindasnormal()

    def morning(self):
        deathlist = self.uc.dayoff()
#        gmorning(deathlist)

#        self.uc.votekill(auservoted(checkAlive))

    def night(self):
        GodSays.closeEyeAll()
        for i in len(Rules.Night):
            actfirstnight(Rules.Night[i])

    def gameprocess(self):
        Prompt.dispatch()
        self.firstnight()
        Ask.forChief()
        while True:
            self.morning()
            self.night()


ff = wolfman()
while True:
    ff.gameprocess()
