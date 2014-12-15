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

        for i in Rules.FirstNight:
            if Settings.rolelist[i] != 0:
                actfirstnight(i)
        usercontrol.firstNightEnd()

    def morning(self):
        deathlist = usercontrol.morningCheck()
        GodSays.dawn(deathlist)
#        gmorning(deathlist)

        usercontrol.votekill(Ask.userVoted(Check.alive))

    def night(self):
        GodSays.closeEyeAll()
        for i in Rules.Night:
            if Settings.rolelist[i] != 0:
             actnight(i)

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
