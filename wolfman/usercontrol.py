from gamerole import *

class usercontrol:
    def __init__(self, gamerole):
        self.gamerole = gamerole

        self.lastguard = 0
        self.guardeduser = 0
        
        self.ispoisoned = False
        self.poisoneduser = 0
        self.issaved = False
        self.saveduser = 0

        self.killed = 0

        self.couple1 = 0
        self.couple2 = 0
        
        self.userlist = [['玩家'+ str(i), '存活', "角色未定义"] \
                         for i in range(gamerole.numtotal + 1)]        

    def setuser(self, u1, role):
        self.userlist[u1][2] = role

    def setcouple(self, u1, u2):
        if not u1 == 0 and not u2 == 0:
            self.userlist[u1].append("情侣")
            self.userlist[u2].append("情侣")
            self.couple1 = u1
            self.couple2 = u2
            return True
        return False

    def printuserstate(self):
        print("\n")
        for i in range(1, self.gamerole.numtotal + 1):
            print(self.userlist[i])

    def coupledeathcheck(self, u1):
        if u1 == self.couple1:
            return self.couple2
        elif u1 == self.couple2:
            return self.couple1
        else:
            return 0

    def setremindasnormal(self):
        for i in range(1, self.gamerole.numtotal + 1):
            if self.userlist[i][2] == "角色未定义":
                self.userlist[i][2] = "平民"

    def death(self, u1, reason):
        self.userlist[u1][1] = reason

    def dayoff(self):
        if self.guarduser == self.killed:
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

        self.guarduser = 0
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
        if u1 == 0:
            return False
        if u1 == self.lastguard:
            return False
        self.lastguard = self.guarduser = u1
        return True

    def witchsave(self):
        if self.issaved:
            return
        if self.killed == 0:
            return

        self.issaved = True
        self.saveduser = self.killed

    def witchpoison(self, u1):
        if self.ispoisoned:
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
        
        
