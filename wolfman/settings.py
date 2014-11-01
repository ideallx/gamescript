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
10人以上给盗贼
'''

from rule import Roles

(SetByDefault, SetByUser, SetByPrompt) = range(3)

rolelist = [0 for i in range(Roles.TotalRoles)]

class Settings:
    def playernumcheck(playernum):
        actual = 0
        for i in range(1, TotalRoles):
            actual += rolelist[i]

        if rolelist[Thief]:
            return actual == playernum + 2
        else:
            return actual == playernum

    def playerRoles(setType, playerlist = []):
        if selType == SetByDefault:
            byDefault()
        elif selType == SetByUser:
            byUser()
        else:
            byPrompt(playerlist)

    def byDefault():
        self.numtotal = gtotaluser
        assert playernum < 19 and playernum > 5
        rolelist[Witch] = 1
        rolelist[Wolves] = 2
        rolelist[Humen] = playernum - 3
        if playernum > 7:
            rolelist[Cupid] = 1
            rolelist[Humen] = playernum - 4
        if playernum > 9:
            rolelist[Thief] = 1
            rolelist[Wolves] = 3
            rolelist[Predict] = 1
            rolelist[Humen] = playernum - 6
        if playernum > 11:
            rolelist[Guard] = 1
            rolelist[Hybird] = 1
            rolelist[Humen] = playernum - 8
        if playernum > 13:
            rolelist[Wolves] = 4
            rolelist[Hunter] = 1
            rolelist[Humen] = playernum - 10
        if playernum > 15:
            rolelist[President] = 1
            rolelist[Humen] = playernum - 11
        if playernum > 16:
            rolelist[Wolves] = 5
            rolelist[Humen] = playernum - 12
        if playernum > 17:
            rolelist[Idiot] = 1
            rolelist[Humen] = playernum - 13

        if rolelist[Thief] == 1:
            rolelist[Humen] += 2

    def byUser():
        rolelist[Thief] = 0
        rolelist[Wolves] = 0
        rolelist[Humen] = 0
        rolelist[Witch] = 0
        rolelist[Cupid] = 0
        rolelist[Predict] = 0
        rolelist[Hybird] = 0
        rolelist[Hunter] = 0
        rolelist[President] = 0
        rolelist[Idiot] = 0
        rolelist[Girl] = 0
        
    def byPrompt(playerlist):
        rolelist = playerlist

