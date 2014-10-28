# -*- coding: utf-8 -*- 

from getinput import *
from gamerole import *
from usercontrol import *

class wolfman:
    def __init__(self):
        self.__playercount = 0
        self.__gamerole = gamerole()
        
        self.getplayernum()
        self.setbattlefield()
        self.dispatchroles()

    def askformat(self, prompt):
        return "\n>>>" + prompt

    def getusernum(self, prompt):
        s = input(prompt + ": ")
        if s == "i":
            self.__userctrl.printuserinfo()
        elif s == "h":
            print("输入i获取所有人信息")
        elif s == "l":
            self.__userctrl.printuserstate()

        if not type(s) is int and not s.isdigit():
            return self.getusernum(prompt)
        i = int(s) 
        if i < 0 or i > self.__playercount:
            return self.getusernum(prompt)
        return i

    def getplayernum(self):
        i = getnum("输入玩家数量")
        if i > 19 or i < 5:
            print("人数不对")
            self.getplayernum(self)
            return
        self.__playercount = i

    def setuser(self, role):
        while True:
            i = self.getusernum("请输入" + role + "号码，输入0表示没有" + role)
            if self.__userctrl.setuser(i,  role) == True:
                return
            else:
                print("该用户已有角色" + self.__userctrl.userlist[i][2])
    
    def setusers(self, num, role):     
        for j in range(self.__gamerole.numwolf):
            self.setuser(role)
        self.__userctrl.wolfkill(self.getusernum("狼人选择杀几号？，输入0表示没有杀人"))

    def setbattlefield(self):
        self.__gamerole.isneedthief()
        self.__gamerole.setbydefault(self.__playercount)
        self.__userctrl = usercontrol(self.__gamerole)

    def dispatchroles(self):
        print("分发身份卡")

    def setcouple(self, c1, c2):
	    return

    def firstnight(self):
        print(self.askformat("天黑请闭眼"))
        if self.__gamerole.hasthief:
            print(self.askformat("盗贼请睁眼"))
            print("记住盗贼身份，请在之后输入")
            print(self.askformat("盗贼请闭眼"))

        if self.__gamerole.hascupid:
            print(self.askformat("丘比特请睁眼"))
            self.setuser("丘比特")
                
            u1 = self.getusernum("请选择情侣第1人，输入0表示没有情侣")
            u2 = self.getusernum("请选择情侣第2人，输入0表示没有情侣")
            if self.__userctrl.setcouple(u1, u2):
                print(str(u1) + "号和" + str(u2) + "为情侣")
            else:
                print("本局没有情侣")
            print(self.askformat("丘比特请闭眼"))
            
            print(self.askformat("情侣请睁眼互认"))
            print(self.askformat("情侣请闭眼"))
                    
        if self.__gamerole.hasguard:
            print(self.askformat("守卫请睁眼"))
            self.setuser("守卫")
            while (True):
                if self.__userctrl.guard(self.getusernum(self.askformat("守卫请选择一个人守护"))) == True:
                    break
            print(self.askformat("守卫请闭眼"))

        print(self.askformat("狼人们请睁眼"))   
        self.setusers(self.__gamerole.numwolf, "狼人")
        print(self.askformat("狼人们请闭眼"))

        if self.__gamerole.haspredict:
            print(self.askformat("预言家请睁眼"))
            self.setuser("预言家")

            i = self.getusernum(self.askformat("预言家想要验谁"))
            if self.__userctrl.iswolf(i):
                print(str(i) + "号是狼人")
            else:
                print(str(i) + "号不是狼人")
            print(self.askformat("预言家请闭眼"))

        if self.__gamerole.haswitch:
            print(self.askformat("女巫请睁眼"))
            self.setuser("女巫")
                
            b = getbool(self.askformat("今天晚上" + str(self.__userctrl.killed) + "号被杀死了，你是否要救"))
            if b:
                self.__userctrl.witchsave()

            i = self.getusernum(self.askformat("是否使用毒药，你要毒谁，输入0表示放弃毒人"))
            self.__userctrl.witchpoison(i)
            print(self.askformat("女巫请闭眼"))

        if self.__gamerole.hashunter:
            print(self.askformat("猎人请睁眼，认识一下"))
            self.setuser("猎人")
            print(self.askformat("猎人请闭眼"))

        self.__userctrl.setremindasnormal()

    def morning(self):
        deathlist = self.__userctrl.dayoff()
        if len(deathlist) == 0:
            print(self.askformat("平安夜"))
            print(self.askformat("警左发言"))
        else:
            print(self.askformat("死了" + str(deathlist)))
            print(self.askformat("死左发言"))

        i = self.getusernum("今天晚上被票死的是")
        self.__userctrl.votekill(i)

    def night(self):
        print(self.askformat("天黑请闭眼"))
        
        if self.__gamerole.hasguard:
            print(self.askformat("守卫请睁眼"))
            while (True):
                if self.__userctrl.guard(self.getusernum(self.askformat("守卫请选择一个人守护"))) == True:
                    break
            print(self.askformat("守卫请闭眼"))

        print(self.askformat("狼人们请睁眼，选择杀一个"))
        self.__userctrl.wolfkill(self.getusernum("狼人选择杀几号？，输入0表示没有杀人"))
        print(self.askformat("狼人们请闭眼"))

        if self.__gamerole.haspredict:
            i = self.getusernum(self.askformat("预言家想要验谁"))
            if self.__userctrl.iswolf(i):
                print(str(i) + "号是狼人")
            else:
                print(str(i) + "号不是狼人")
            print(self.askformat("预言家请闭眼"))

        if self.__gamerole.haswitch:
            print(self.askformat("女巫请睁眼"))
            b = getbool(self.askformat("今天晚上" + str(self.__userctrl.killed) + "号被杀死了，你是否要救"))
            if b:
                self.__userctrl.witchsave()

            i = self.getusernum(self.askformat("是否使用毒药，你要毒谁，输入0表示放弃毒人"))
            self.__userctrl.witchpoison(i)
            print(self.askformat("女巫请闭眼"))

    def gameprocess(self):
        self.firstnight()
        input(self.askformat("天亮了，竞选警长"))
        while True:
            self.morning()
            self.night()

ff = wolfman()
ff.gameprocess()
