# -*- coding: utf-8 -*- 

from getinput import *
from gamerole import *
from usercontrol import *
from gameprompt import *
    
class wolfman:
    def __init__(self):
        self.gr = gamerole()
        self.uc = usercontrol()
        
        gameinit(aplayernum(checkUserNum))

        self.gr.isneedthief(ahasthief())
        self.gr.setbydefault(gtotaluser)

    def firstnight(self):
        gallcloseeye()

        actfirstnight(Thief)
        actfirstnight(Cupid)
        actfirstnight(Guard):
        actfirstnight(Wolves)  
        actfirstnight(Predict):
        actfirstnight(Witch):
        actfirstnight(Hunter):

        self.uc.setremindasnormal()

    def morning(self):
        deathlist = self.uc.dayoff()
        gmorning(deathlist)

        self.uc.votekill(auservoted(checkAlive))

    def night(self):
        gallcloseeye()
        
        actnight(Guard):
        actnight(Predict):
        actnight(Witch):

    def gameprocess(self):
        pdispatchrole()
        self.firstnight()
        aforchief()
        while True:
            self.morning()
            self.night()

ff = wolfman()

while True:
    ff.gameprocess()
