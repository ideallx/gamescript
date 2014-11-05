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

from rule import Rules

(SetByDefault, SetByUser, SetByPrompt) = range(3)


class Settings:
    rolelist = [0 for i in range(Rules.TotalRoles)]
    playerNum = 0

    def playernumcheck(playernum):
        actual = 0
        for i in range(1, TotalRoles):
            actual += Settings.rolelist[i]

        Settings.playerNum = playernum

        if Settings.rolelist[Thief]:
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
        Settings.rolelist[Witch] = 1
        Settings.rolelist[Wolves] = 2
        Settings.rolelist[Humen] = playernum - 3
        if playernum > 7:
            Settings.rolelist[Cupid] = 1
            Settings.rolelist[Humen] = playernum - 4
        if playernum > 9:
            Settings.rolelist[Thief] = 1
            Settings.rolelist[Wolves] = 3
            Settings.rolelist[Predict] = 1
            Settings.rolelist[Humen] = playernum - 6
        if playernum > 11:
            Settings.rolelist[Guard] = 1
            Settings.rolelist[Hybird] = 1
            Settings.rolelist[Humen] = playernum - 8
        if playernum > 13:
            Settings.rolelist[Wolves] = 4
            Settings.rolelist[Hunter] = 1
            Settings.rolelist[Humen] = playernum - 10
        if playernum > 15:
            Settings.rolelist[President] = 1
            Settings.rolelist[Humen] = playernum - 11
        if playernum > 16:
            Settings.rolelist[Wolves] = 5
            Settings.rolelist[Humen] = playernum - 12
        if playernum > 17:
            Settings.rolelist[Idiot] = 1
            Settings.rolelist[Humen] = playernum - 13

        if Settings.rolelist[Thief] == 1:
            Settings.rolelist[Humen] += 2

    def byUser():
        Settings.rolelist[Thief] = 0
        Settings.rolelist[Wolves] = 0
        Settings.rolelist[Humen] = 0
        Settings.rolelist[Witch] = 0
        Settings.rolelist[Cupid] = 0
        Settings.rolelist[Predict] = 0
        Settings.rolelist[Hybird] = 0
        Settings.rolelist[Hunter] = 0
        Settings.rolelist[President] = 0
        Settings.rolelist[Idiot] = 0
        Settings.rolelist[Girl] = 0
        
    def byPrompt(playerlist):
        Settings.rolelist = playerlist

