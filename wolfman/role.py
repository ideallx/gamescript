# -*- coding: utf-8 -*- 
from gameinfo import *
from gameprompt import *

def setuserroleinput(roleid, userseq = 0):
    return asetuserrole(roleid, checkSetRole, userseq)

def setuser(uid, roleid):
    if roleid == RWolves:
        guserlist[uid] = RoleWolf(uid)
    elif roleid == RWitch:
        guserlist[uid] = RoleWitch(uid)
    elif roleid == RHumen:
        guserlist[uid] = RoleHumen(uid)

class RoleHuman:
    uid = 0
    live = LUndead
    role = RReserved
    camp = CUndecided
    
    def __init__(self, uid):
        self.uid  = uid
        self.live = LUndead
        
        self.role = RHumen
        self.camp = CUndecided

    #first night act
    def fnact():
        return;

    #normal night act
    def nact(self):
        return

    def killed(self, reason):
        self.live = reason
        return

    def display(self):
        return

class RoleGods(RoleHuman):
    def __init(self, uid):
        self.camp = CGods

    def fnact():
        setuser(setuserroleinput(self.role, i), self.role)



class RoleWolf(RoleHuman):
    def __init__(self, uid):
        self.role = RWolves
        self.camp = CWolves

    def fnact():
        for i = range(grolelist[self.role]):
            setuser(setuserroleinput(self.role, i), self.role)

    def nact(self):
        wolfkill(achooseuser(checkAlive))

    def display(self):
        print(self.users)


class RoleWitch(RoleGods):
    drugsave = 1
    drugpoison = 1
    def __init__(self, uid):
        self.role = RWitch

    def nact(self):

