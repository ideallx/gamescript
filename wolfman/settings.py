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

from rule import *

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
        Settings.rolelist[Rules.Witch] = 1
        Settings.rolelist[Rules.Wolves] = 2
        Settings.rolelist[Rules.Humen] = Settings.playerNum - 3
        if Settings.playerNum > 7:
            Settings.rolelist[Rules.Cupid] = 1
            Settings.rolelist[Rules.Humen] = Settings.playerNum - 4
        if Settings.playerNum > 9:
            Settings.rolelist[Rules.Thief] = 1
            Settings.rolelist[Rules.Wolves] = 3
            Settings.rolelist[Rules.Predict] = 1
            Settings.rolelist[Rules.Humen] = Settings.playerNum - 6
        if Settings.playerNum > 11:
            Settings.rolelist[Rules.Guard] = 1
            Settings.rolelist[Rules.Hybird] = 1
            Settings.rolelist[Rules.Humen] = Settings.playerNum - 8
        if Settings.playerNum > 13:
            Settings.rolelist[Rules.Wolves] = 4
            Settings.rolelist[Rules.Hunter] = 1
            Settings.rolelist[Rules.Humen] = Settings.playerNum - 10
        if Settings.playerNum > 15:
            Settings.rolelist[Rules.President] = 1
            Settings.rolelist[Rules.Humen] = Settings.playerNum - 11
        if Settings.playerNum > 16:
            Settings.rolelist[Rules.Wolves] = 5
            Settings.rolelist[Rules.Humen] = Settings.playerNum - 12
        if Settings.playerNum > 17:
            Settings.rolelist[Rules.Idiot] = 1
            Settings.rolelist[Rules.Humen] = Settings.playerNum - 13

        if Settings.rolelist[Rules.Thief] == 1:
            Settings.rolelist[Rules.Humen] += 2

    def byUser():
        Settings.rolelist[Rules.Thief] = 0
        Settings.rolelist[Rules.Wolves] = 0
        Settings.rolelist[Rules.Humen] = 0
        Settings.rolelist[Rules.Witch] = 0
        Settings.rolelist[Rules.Cupid] = 0
        Settings.rolelist[Rules.Predict] = 0
        Settings.rolelist[Rules.Hybird] = 0
        Settings.rolelist[Rules.Hunter] = 0
        Settings.rolelist[Rules.President] = 0
        Settings.rolelist[Rules.Idiot] = 0
        Settings.rolelist[Rules.Girl] = 0
        
    def byPrompt(playerlist):
        Settings.rolelist = playerlist

