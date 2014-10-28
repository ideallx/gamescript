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

    def getusernum(self, prompt):
        s = input(prompt + ": ")
        if s == "i":
            self.__userctrl.printuserstate()
        elif s == "h":
            print("输入i获取所有人信息")

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

    def setbattlefield(self):
        self.__gamerole.isneedthief()
        self.__gamerole.setbydefault(self.__playercount)
        self.__userctrl = usercontrol(self.__gamerole)

    def dispatchroles(self):
        print("分发身份卡")

    def setcouple(self, c1, c2):
	    return

    def firstnight(self):
        print("\n>>>天黑请闭眼")
        if self.__gamerole.hasthief:
            print("\n>>>盗贼请睁眼")
            print("记住盗贼身份，请在之后输入")
            print("\n>>>盗贼请闭眼")

        if self.__gamerole.hascupid:
            print("\n>>>丘比特请睁眼")
            i = self.getusernum("输入丘比特号码，输入0表示没有丘比特")
            self.__userctrl.setuser(i, "丘比特")
                
            u1 = self.getusernum("请选择情侣第1人，输入0表示没有情侣")
            u2 = self.getusernum("请选择情侣第2人，输入0表示没有情侣")
            if self.__userctrl.setcouple(u1, u2):
                print(str(u1) + "号和" + str(u2) + "为情侣")
            else:
                print("本局没有情侣")
            print("\n>>>丘比特请闭眼")
                    
        if self.__gamerole.hasguard:
            print("\n>>>守卫请睁眼")
            i = self.getusernum("输入守卫号码，输入0表示没有守卫")
            self.__userctrl.setuser(i, "守卫")
            while (True):
                if self.__userctrl.guard(self.getusernum("\n>>>守卫请选择一个人守护")) == True:
                    break
            print("\n>>>守卫请闭眼")

        print("\n>>>狼人们请睁眼，选择杀一个")
        for j in range(self.__gamerole.numwolf):
            i = self.getusernum("输入狼人" + str(j + 1) + "号号码，输入0表示没有狼人")
            if not i == 0:
                self.__userctrl.setuser(i, "狼人")
        self.__userctrl.wolfkill(self.getusernum("狼人选择杀几号？，输入0表示没有杀人"))
        print("\n>>>狼人们请闭眼")

        if self.__gamerole.haspredict:
            print("\n>>>预言家请睁眼")
            i = self.getusernum("输入预言家号码，输入0表示没有预言家")
            self.__userctrl.setuser(i, "预言家")

            i = self.getusernum("\n>>>预言家想要验谁")
            if self.__userctrl.iswolf(i):
                print(str(i) + "号是狼人")
            else:
                print(str(i) + "号不是狼人")
            print("\n>>>预言家请闭眼")

        if self.__gamerole.haswitch:
            print("\n>>>女巫请睁眼")
            i = self.getusernum("输入女巫号码，输入0 表示没有女巫")
            self.__userctrl.setuser(i, "女巫")
                
            b = getbool("\n>>>今天晚上" + str(self.__userctrl.killed) + "号被杀死了，你是否要救")
            if b:
                self.__userctrl.witchsave()

            i = self.getusernum("\n>>>是否使用毒药，你要毒谁，输入0表示放弃毒人")
            self.__userctrl.witchpoison(i)
            print("\n>>>女巫请闭眼")

        if self.__gamerole.hashunter:
            print("\n>>>猎人请睁眼，认识一下")
            i = self.getusernum("输入猎人号码，输入0 表示没有猎人")
            self.__userctrl.setuser(i, "猎人")
            print("\n>>>猎人请闭眼")

        self.__userctrl.setremindasnormal()

    def morning(self):
        deathlist = self.__userctrl.dayoff()
        if len(deathlist) == 0:
            print("\n>>>平安夜")
            print("\n>>>警左发言")
        else:
            print("\n>>>死了" + str(deathlist))
            print("\n>>>死左发言")

        i = self.getusernum("今天晚上被票死的是")
        self.__userctrl.votekill(i)

    def night(self):
        print("\n>>>天黑请闭眼")
        
        if self.__gamerole.hasguard:
            print("\n>>>守卫请睁眼")
            while (True):
                if self.__userctrl.guard(self.getusernum("\n>>>守卫请选择一个人守护")) == True:
                    break
            print("\n>>>守卫请闭眼")

        print("\n>>>狼人们请睁眼，选择杀一个")
        self.__userctrl.wolfkill(self.getusernum("狼人选择杀几号？，输入0表示没有杀人"))
        print("\n>>>狼人们请闭眼")

        if self.__gamerole.haspredict:
            i = self.getusernum("\n>>>预言家想要验谁")
            if self.__userctrl.iswolf(i):
                print(str(i) + "号是狼人")
            else:
                print(str(i) + "号不是狼人")
            print("\n>>>预言家请闭眼")

        if self.__gamerole.haswitch:
            print("\n>>>女巫请睁眼")
            b = getbool("\n>>>今天晚上" + str(self.__userctrl.killed) + "号被杀死了，你是否要救")
            if b:
                self.__userctrl.witchsave()

            i = self.getusernum("\n>>>是否使用毒药，你要毒谁，输入0表示放弃毒人")
            self.__userctrl.witchpoison(i)
            print("\n>>>女巫请闭眼")

    def gameprocess(self):
        self.firstnight()
        input("\n>>>天亮了，竞选警长")
        while True:
            self.morning()
            self.night()

ff = wolfman()
ff.gameprocess()
