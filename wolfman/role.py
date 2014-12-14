# -*- coding: utf-8 -*- 
from gameprompt import *
from usercontrol import *

class RoleHuman:
    usersid = []
    role = Rules.Reserved
    camp = Camps.Undecided

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
        usercontrol.setUserRole(userid, self.role)
        usercontrol.setUserCamp(userid, self.camp)

    def display(self):
        return

    def isUserAlive(self):
        if len(self.usersid) == 0:
            return False
        return usercontrol.userlist[self.usersid[0]].livestate == LiveStates.Undead

    
class RoleThief(RoleHuman):
    def fnact(self):
        Prompt.thiefNight()


class RoleGods(RoleHuman):
    camp = Camps.Gods

    def fnact(self):
        userid = Ask.setUserRole(self.role, Check.setRole)
        if userid != 0:
            self.addUser(userid)



class RoleWolf(RoleHuman):
    role = Rules.Wolves
    camp = Camps.Wolves

    def fnact(self):
        for i in range(1, Settings.rolelist[Rules.Wolves] + 1):
            self.addUser(Ask.setUserRole(self.role, Check.setRole, i))

    def nact(self):
        usercontrol.killed = Ask.chooseUser(Check.alive)


class RoleWitch(RoleGods):
    drugsave = 1
    drugpoison = 1
    role = Rules.Witch

    def nact(self):
        if Ask.useSave(usercontrol.killed) and self.drugsave and self.isUserAlive():
            usercontrol.saved = usercontrol.killed
            self.drugsave = 0
        poisoned = Ask.usePoison(Check.alive)
        if poisoned and self.drugpoison and self.isUserAlive():
            usercontrol.poisoned = poisoned
            self.drugpoison = 0

class RoleCupid(RoleGods):
    role = Rules.Cupid

    def fnact(self):
        super(RoleCupid, self).fnact()
        if not self.isUserAlive():
            return
        usercontrol.couple1 = Ask.setCouple(1, Check.setCouple)
        usercontrol.couple2 = Ask.setCouple(2, Check.setCouple)

    def anact(self):
        GodSays.openEyeCouple()
        GodSays.closeEyeCouple()


class RolePredict(RoleGods):
    role = Rules.Predict

    def nact(self):
        user = Ask.chooseUser(Check.alive)
        if not self.isUserAlive():
            return
        Prompt.isWolf(user, usercontrol.isWolf(user))

class RoleGuard(RoleGods):
    role = Rules.Guard

    def nact(self):
        guarded = Ask.chooseUser(Check.alive)
        if not self.isUserAlive():
            return
        usercontrol.guarded = guarded

class RoleHybird(RoleGods):
    role = Rules.Hybird

class RoleHunter(RoleGods):
    role = Rules.Hunter

class RolePresident(RoleGods):
    role = Rules.President

class RoleIdiot(RoleGods):
    role = Rules.Idiot

class RoleGirl(RoleGods):
    role = Rules.Girl

class RoleReserved(RoleHuman):
    role = Rules.Reserved

        
class Roles:
    rolelist = [RoleReserved(), RoleThief(), RoleWolf(), RoleHuman(), \
                RoleWitch(), RoleCupid(), RolePredict(), RoleGuard(), \
                RoleHybird(), RoleHunter(), RolePresident(), RoleIdiot(), \
                RoleGirl()]

    def getRole(roleid):
        return Roles.rolelist[roleid]
