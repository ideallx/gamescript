# -*- coding: utf-8 -*- 

from getinput import *
from gamerole import *
from usercontrol import *


def askformat(prompt):
    return "\n>>>" + prompt

def openeye(role):
    print(askformat(rolename[role] + "请睁眼"))

def closeeye(role):
    print(askformat(rolename[role] + "请睁眼"))
    
class wolfman:
    def __init__(self):
        self.__playercount = 0
        self.__gamerole = gamerole()
        
        self.getplayernum()
        self.setbattlefield()
        self.dispatchroles()

    def hasRole(self, roleid):
        return self.__gamerole.rolelist[roleid]

    def getusernum(self, prompt):
        s = input(prompt + ": ")
        if s == "i":
            self.uc.printuserinfo()
        elif s == "h":
            print("输入 \"i\" 获取所有人信息")
            print("输入 \"l\" 获取存活玩家信息")
            print("输入 \"k 3\" 杀死3号玩家")
            print("输入 \"a 3\" 救起3号玩家")
            print("输入 \"c 1 2\" 设置1号2号玩家为情侣")
            print("输入 \"o\" 获取所有角色的角色号")
            print("输入 \"r 3 2\" 设置3号玩家的角色为2")
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
        i = getnum("输入玩家数量")
        if i > 18 or i < 6:
            print("人数不对")
            self.getplayernum()
            return
        self.__playercount = i

    def setuser(self, role):
        while True:
            i = self.getusernum("请输入" + rolename[role] + "号码，输入0表示没有" + rolename[role])
            if self.uc.setuser(i,  role):
                return
            else:
                print("该用户已有角色" + self.uc.userlist[i][Role])
    
    def setusers(self, num, role):     
        for j in range(num):
            self.setuser(role)

    def setbattlefield(self):
        self.__gamerole.isneedthief()
        self.__gamerole.setbydefault(self.__playercount)
        self.uc = usercontrol(self.__gamerole)

    def dispatchroles(self):
        print("分发身份卡")

    def setcouple(self, c1, c2):
	    return

    def firstnight(self):
        print(askformat("天黑请闭眼"))

        if self.hasRole(Thief):
            openeye(Thief)
            print("记住盗贼身份，请在之后输入")
            closeeye(Thief)

        if self.hasRole(Cupid):
            openeye(Cupid)
            self.setuser(Cupid)
                
            u1 = self.getusernum("请选择情侣第1人，输入0表示没有情侣")
            u2 = self.getusernum("请选择情侣第2人，输入0表示没有情侣")
            if self.uc.setcouple(u1, u2):
                print(str(u1) + "号和" + str(u2) + "为情侣")
            else:
                print("本局没有情侣")
            closeeye(Cupid)
            
            print(askformat("情侣请睁眼互认"))
            print(askformat("情侣请闭眼"))
                    
        if self.hasRole(Guard):
            print(askformat("守卫请睁眼"))
            self.setuser(Guard)
            while (True):
                if self.uc.guard(self.getusernum(askformat("守卫请选择一个人守护"))) == True:
                    break
            print(askformat("守卫请闭眼"))

        print(askformat("狼人们请睁眼"))   
        self.setusers(self.hasRole(Wolves), Wolves)
        self.uc.wolfkill(self.getusernum("狼人选择杀几号？，输入0表示没有杀人"))
        print(askformat("狼人们请闭眼"))

        if self.hasRole(Predict):
            print(askformat("预言家请睁眼"))
            self.setuser(Predict)

            i = self.getusernum(askformat("预言家想要验谁"))
            if self.uc.iswolf(i):
                print(str(i) + "号是狼人")
            else:
                print(str(i) + "号不是狼人")
            print(askformat("预言家请闭眼"))

        if self.hasRole(Witch):
            print(askformat("女巫请睁眼"))
            self.setuser(Witch)
                
            b = getbool(askformat("今天晚上" + str(self.uc.killed) + "号被杀死了，你是否要救"))
            if b:
                self.uc.witchsave()

            i = self.getusernum(askformat("是否使用毒药，你要毒谁，输入0表示放弃毒人"))
            self.uc.witchpoison(i)
            print(askformat("女巫请闭眼"))

        if self.self.hasRole(Hunter):
            print(askformat("猎人请睁眼，认识一下"))
            self.setuser(Hunter)
            print(askformat("猎人请闭眼"))

        self.uc.setremindasnormal()

    def morning(self):
        deathlist = self.uc.dayoff()
        if len(deathlist) == 0:
            print(askformat("平安夜"))
            print(askformat("警左发言"))
        else:
            print(askformat("死了" + str(deathlist)))
            print(askformat("死左发言"))

        i = self.getusernum("今天晚上被票死的是")
        self.uc.votekill(i)

    def night(self):
        print(askformat("天黑请闭眼"))
        
        if self.__gamerole.hasguard:
            print(askformat("守卫请睁眼"))
            while (True):
                if self.uc.guard(self.getusernum(askformat("守卫请选择一个人守护"))) == True:
                    break
            print(askformat("守卫请闭眼"))

        print(askformat("狼人们请睁眼，选择杀一个"))
        self.uc.wolfkill(self.getusernum("狼人选择杀几号？，输入0表示没有杀人"))
        print(askformat("狼人们请闭眼"))

        if self.__gamerole.haspredict:
            i = self.getusernum(askformat("预言家想要验谁"))
            if self.uc.iswolf(i):
                print(str(i) + "号是狼人")
            else:
                print(str(i) + "号不是狼人")
            print(askformat("预言家请闭眼"))

        if self.__gamerole.haswitch:
            print(askformat("女巫请睁眼"))
            b = getbool(askformat("今天晚上" + str(self.uc.killed) + "号被杀死了，你是否要救"))
            if b:
                self.uc.witchsave()

            i = self.getusernum(askformat("是否使用毒药，你要毒谁，输入0表示放弃毒人"))
            self.uc.witchpoison(i)
            print(askformat("女巫请闭眼"))

    def gameprocess(self):
        self.firstnight()
        input(askformat("天亮了，竞选警长"))
        while True:
            self.morning()
            self.night()

ff = wolfman()
ff.gameprocess()
