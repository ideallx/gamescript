# -*- coding: utf-8 -*- 
'''
6-7人   2狼人 1女巫 3-4个村民 
8-9人   2狼人 1女巫 1爱神 4-5个民
10-11人 3狼人 1先知 1女巫 1爱神 4-5个民。
12-13人 3狼人 1先知 1女巫 1爱神 1守护 1混血 4-5民。
14-15人 4狼人 1先知 1女巫 1爱神 1守护 1猎人 1混血  4-5民
16人    4狼人 1先知 1女巫 1爱神 1守护 1猎人 1村长 1混血 5个民
17人    5狼人 1先知 1女巫 1爱神 1守护 1猎人 1村长 1混血 5个民
18人    5狼人 1先知 1女巫 1爱神 1守护 1猎人 1村长 1白痴 1混血 5个民
'''

from getinput import *

class gamerole:
    isextend = False

    hasthief = False
    hascupid = False
    haswitch = False
    hasguard = False
    hashunter = False
    hashybird = False
    haspredict = False
    haspresident = False
    hasidiot = False
    hasgirl = False

    numwolf = 0
    numhuman = 0
    numtotal = 0

    def isneedthief(self):
        self.hasthief = getbool("是否启用盗贼")

    def setbydefault(self, playernum):
        self.numtotal = playernum
        assert playernum < 20 and playernum > 5
        self.haswitch = True
        self.numwolf = 2
        self.numhuman = playernum - 3
        if playernum > 7:
            self.hascupid = True
            self.numhuman = playernum - 4
        if playernum > 9:
            self.numwolf = 3
            self.haspredict = True
            self.numhuman = playernum - 6
        if playernum > 11:
            self.hasguard = True
            self.hashybird = True
            self.numhuman = playernum - 8
        if playernum > 13:
            self.numwolf = 4
            self.hashunter = True
            self.numhuman = playernum - 10
        if playernum > 15:
            self.haspresident = True
            self.numhuman = playernum - 11
        if playernum > 16:
            self.numwolf = 5
            self.numhuman = playernum - 12
        if playernum > 17:
            self.hasidiot = True
            self.numhuman = playernum - 13

        if self.hasthief == True:
            self.numwolf += 1
            self.numhuman += 1
        self.printall()

    def printall(self):
        if self.isextend:
            print("启用扩展包")
        else:
            print("不启用扩展包")

        if self.hasthief:
            print("启用盗贼")
        else:
            print("不启用盗贼")
        if self.hascupid:
            print("启用丘比特")
        if self.haswitch:
            print("启用女巫")
        if self.hasguard:
            print("启用守卫")
        if self.hashunter:
            print("启用猎人")
        if self.hashybird:
            print("启用混血儿")
        if self.haspredict:
            print("启用预言家")
        if self.haspresident:
            print("启用村长")
        if self.hasidiot:
            print("启用白痴")
        if self.hasgirl:
            print("启用小女孩")

        print (str(self.numwolf) + "个狼人")
        print (str(self.numhuman) + "个村民")
