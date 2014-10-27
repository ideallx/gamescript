# -*- coding: utf-8 -*- 

from getinput import *
from gamerole import *

class wolfman:
    def __init__(self):
        self.__playercount = 0
        self.__gamerole = gamerole()
        self.__userlist = []

        self.__guardnum = 0
        self.__saved = False
        self.__poisoned = False
        self.__killed = 0

    def getusernum(self, prompt):
        i = getnum(prompt)
        if i < 0 or i > self.__playercount:
            self.getusernum(prompt)
        return i

    def getplayernum(self):
        i = getnum("输入玩家数量")
        if i > 19 or i < 5:
            print("人数不对")
            self.getplayernum(self)
            return
        self.__playercount = i
        self.__userlist = [["角色未定义", "存活"] for i in range(i)]

    def beforegame(self):
        self.getplayernum()
        self.setbattlefield()
        self.dispatchroles()

    def setbattlefield(self):
        self.__gamerole.isneedthief()
        self.__gamerole.setbydefault(self.__playercount)

    def dispatchroles(self):
        input("分发身份卡")

    def setuser(self, userid, role):
        self.__userlist[userid - 1] = role
        print(self.__userlist)

    def setcouple(self, c1, c2):

    def firstnight(self):
        input("\n天黑请闭眼")
        if self.__gamerole.hasthief:
            input("\n盗贼请睁眼\n")
            print("记住盗贼身份，请在之后输入")
            input("盗贼请闭眼")

        if self.__gamerole.hascupid:
            input("\n丘比特请睁眼\n")
            i = self.getusernum("输入丘比特号码，输入0 表示没有丘比特")
            if not i == 0:
                input("\n请选择两个人作为情侣")

        if self.__gamerole.hasguard:
            input("\n守卫请睁眼\n")
            i = self.getusernum("输入守卫号码，输入0 表示没有守卫")
            if not i == 0:
                self.setuser(i, "守卫")


        print("\n狼人请睁眼，选择杀一个")
        for j in range(self.__gamerole.numwolf):
            i = self.getusernum("输入狼人" + str(i + 1) + "号号码，输入0 表示没有狼人")
            if not i == 0:
                self.setuser(i, "狼人")
        self.__killed = self.getusernum("狼人选择杀几号？，输入0表示没有杀人")

        if self.__gamerole.haswitch:
            input("\n")
        

    def gameprocess(self):
        self.beforegame()
        self.firstnight()
        self.firstmorning()

ff = wolfman()
ff.gameprocess()
