# -*- coding: utf-8 -*- 

from role import *
from check import *

def actfirstnight(roleid):
    role = Roles.getRole(roleid)
    if role == 0:
        return

    GodSays.openEye(roleid)
    role.fnact()
    role.nact()
    GodSays.closeEye(roleid)

    role.anact()

def actnight(roleid):
    role = Roles.getRole(roleid)

    GodSays.openEye(roleid)
    role.nact()
    GodSays.closeEye(roleid)

    role.anact()
    
class wolfman:
    def __init__(self):
        Settings.playerNum = Ask.playerNums(Check.userNum)
        Settings.byDefault()
        usercontrol.__init__()

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
        GodSays.forChief()
        while True:
            self.morning()
            self.night()


ff = wolfman()
while True:
    ff.gameprocess()
