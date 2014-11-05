# -*- coding: utf-8 -*- 

class Rules:
    TotalRoles = 13
    (Reserved, Thief, Wolves, Humen, Witch, Cupid, Predict, \
    Guard, Hybird, Hunter, President, Idiot, Girl) = range(TotalRoles)
    
    Morning = [Thief, Cupid, Guard, Wolves, Predict, Witch, Hunter]
    Night = [Guard, Predict, Witch]

    MinUsers = 6
    MaxUsers = 18

class Camps:
    TotalCamps = 5
    (Undecided, Wolves, Gods, Humen, Wolfman) = range(TotalCamps)

class LiveStates:
    TotalLiveStates = 5
    (Undead, Voted, Killed, Poisoned, Couple) = range(TotalLiveStates)

class ArrayUser:
    TotalArraySize = 3
    (Roles, LiveState, Camp) = range(TotalArraySize)
