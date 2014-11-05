# -*- coding: utf-8 -*- 
from gameprompt import *
from usercontrol import *

def setuserroleinput(roleid, userseq = 0):
    return asetuserrole(roleid, Check.setRole, userseq)



class RoleHuman:
    usersid = []
    role = 0
    camp = 0
    
    def __init__(self):
        self.role = Rules.Hume
        self.camp = Camps.Hume

    #first night act
    def fnact(self):
        return;

    #normal night act
    def nact(self):
        return

    #after night act
    def anact(self):
        return

    def killed(self, reason):
        self.live = reason
        return

    def addUser(self, userid):
        self.usersid.append(userid)
        usercontrol.setUserRole(uid, self.role)
        usercontrol.setUserCamp(uid, self.camp)

    def display(self):
        return

    
class RoleThief:
    def fnact(self):
        Prompt.thiefNight()


class RoleGods(RoleHuman):
    def __init(self, uid):
        self.camp = CGods
        usercontrol.setUserCamp(uid, Camps.Gods)

    def fnact(self):
        addUser(setuserroleinput(self.role, i))



class RoleWolf(RoleHuman):
    def __init__(self):
        self.role = Rules.Wolves
        self.camp = Camps.Wolves

    def fnact(self):
        for i in range(grolelist[self.role]):
            addUser(setuserroleinput(self.role, i))

    def nact(self):
        usercontrol.killed = Ask.chooseUser(Check.alive)


class RoleWitch(RoleGods):
    drugsave = 1
    drugpoison = 1
    def __init__(self):
        self.role = Rules.Witch

    def nact(self):
        if Ask.useSave(usercontrol.killed) and self.drugsave:
            usercontrol.saved = usercontrol.killed
            self.drugsave = 0
        poisoned = Ask.userPoison(Check.alive)
        if poisoned and self.drugpoison:
            usercontrol.poisoned = poisoned
            self.drugpoison = 0

class RoleCupid(RoleGods):
    def __init__(self):
        self.role = Rules.Cupid

    def fnact(self):
        super(RoleCupid, self).fnact()
        usercontrol.couple1 = Ask.setCouple(1, Check.setCouple)
        usercontrol.couple1 = Ask.setCouple(2, Check.setCouple)

    def anact(self):
        GodSays.openEyeCouple()
        GodSays.closeEyeCouple()


class RolePredict(RoleGods):
    def __init__(self):
        self.role = Rules.Predict

    def nact(self):
        user = Ask.chooseUser(Check.alive)
        Promopt.isWolf(user, usercontrol.isWolf(user))

class RoleGuard(RoleGods):
    def __init__(self):
        self.role = Rules.Guard

    def nact(self):
        usercontrol.guarded = Ask.chooseUser(Check.alive)

class RoleHybird(RoleGods):
    def __init__(self):
        self.role = Rules.Hybird

class RoleHunter(RoleGods):
    def __init__(self):
        self.role = Rules.Hunter

class RolePresident(RoleGods):
    def __init__(self):
        self.role = Rules.President

class RoleIdiot(RoleGods):
    def __init__(self):
        self.role = Rules.Idiot

class RoleGirl(RoleGods):
    def __init__(self):
        self.role = Rules.Girl

class RoleReserved(RoleHuman):
    def __init(self):
        self.role = Rules.Reserved

        
class Roles:
    rolelist = [RoleReserved, RoleThief, RoleWolf, RoleHuman, \
                RoleWitch, RoleCupid, RolePredict, RoleGuard, \
                RoleHybird, RoleHunter, RolePresident, RoleIdiot, \
                RoleGirl]

    def getRole(roleid):
        return Roles.rolelist[roleid]
