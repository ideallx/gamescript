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

totalrole = 13
(Reserved, Thief, Wolves, Humen, Witch, Cupid, Predict, \
 Guard, Hybird, Hunter, President, Idiot, Girl) = range(totalrole)
rolename = ["保留", "盗贼", "狼人", "普通村名", "女巫", "丘比特", "预言家", \
            "守卫", "混血儿", "猎人", "村长", "白痴", "小女孩"] 

from getinput import *
class gamerole:
    numtotal = 0
    rolelist = []

    def isneedthief(self):
        if getbool("是否启用盗贼"):
            self.rolelist[Thief] = 1

    def __init__(self):
        self.rolelist = [0 for i in range(totalrole)]

    def setbydefault(self, playernum):
        self.numtotal = playernum
        assert playernum < 20 and playernum > 5
        self.rolelist[Witch] = 1
        self.rolelist[Wolves] = 2
        self.rolelist[Humen] = playernum - 3
        if playernum > 7:
            self.rolelist[Cupid] = 1
            self.rolelist[Humen] = playernum - 4
        if playernum > 9:
            self.rolelist[Wolves] = 3
            self.rolelist[Predict] = 1
            self.rolelist[Humen] = playernum - 6
        if playernum > 11:
            self.rolelist[Guard] = 1
            self.rolelist[Hybird] = 1
            self.rolelist[Humen] = playernum - 8
        if playernum > 13:
            self.rolelist[Wolves] = 4
            self.rolelist[Hunter] = 1
            self.rolelist[Humen] = playernum - 10
        if playernum > 15:
            self.rolelist[President] = 1
            self.rolelist[Humen] = playernum - 11
        if playernum > 16:
            self.rolelist[Wolves] = 5
            self.rolelist[Humen] = playernum - 12
        if playernum > 17:
            self.rolelist[Idiot] = 1
            self.rolelist[Humen] = playernum - 13

        if self.rolelist[Thief] == 1:
            self.rolelist[Humen] += 2
        self.printall()

    def printall(self):
        if self.rolelist[Thief]:
            print("启用盗贼")
        else:
            print("不启用盗贼")
        if self.rolelist[Cupid]:
            print("启用丘比特")
        if self.rolelist[Witch]:
            print("启用女巫")
        if self.rolelist[Guard]:
            print("启用守卫")
        if self.rolelist[Hunter]:
            print("启用猎人")
        if self.rolelist[Hybird]:
            print("启用混血儿")
        if self.rolelist[Predict]:
            print("启用预言家")
        if self.rolelist[President]:
            print("启用村长")
        if self.rolelist[Idiot]:
            print("启用白痴")
        if self.rolelist[Girl]:
            print("启用小女孩")

        print (str(self.rolelist[Wolves]) + "个狼人")
        print (str(self.rolelist[Humen]) + "个村民")
