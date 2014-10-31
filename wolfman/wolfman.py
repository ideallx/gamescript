# -*- coding: utf-8 -*- 

from getinput import *
from gamerole import *
from usercontrol import *
from gameprompt import *
    
class wolfman:
    def __init__(self):
        self.__playercount = 0
        self.__gamerole = gamerole()
        
        self.getplayernum()
        self.setbattlefield()
        pdispatchrole()

    def hasRole(self, roleid):
        return self.__gamerole.rolelist[roleid]

    def getusernum(self, prompt):
        s = input(prompt + ": ")
        if s == "i":
            self.uc.printuserinfo()
        elif s == "h":
            phelp()
        elif s == "l":
            self.uc.printuserstate()
        elif s == "o":
            print(rolename)

        if not type(s) is int and not s.isdigit():
            return self.getusernum(prompt)
        i = int(s) 
        if i < 0 or i > self.__playercount:
            return self.getusernum(prompt)
        return i

    def getplayernum(self):
        i = aplayernum()
        if i > 18 or i < 6:
            pplayernumerror()
            self.getplayernum()
            return
        self.__playercount = i

    def setuser(self, roleid):
        while True:
            i = asetuserrole(roleid)
            if self.uc.setuser(i,  role):
                return
            else:
                puserhadrole(self.uc.userlist[i][Role])
    
    def setusers(self, num, role):     
        for j in range(num):
            self.setuser(role)

    def setbattlefield(self):
        needthief = ahasthief()
        self.__gamerole.isneedthief(needthief)
        self.__gamerole.setbydefault(self.__playercount)
        self.uc = usercontrol(self.__gamerole)

    def setcouple(self, c1, c2):
	    return

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

        i = auservoted()
        self.uc.votekill(i)

    def night(self):
        gallcloseeye()
        
        actnight(Guard):
        actnight(Predict):
        actnight(Witch):

    def gameprocess(self):
        self.firstnight()
        aforchief()
        while True:
            self.morning()
            self.night()

ff = wolfman()
ff.gameprocess()
