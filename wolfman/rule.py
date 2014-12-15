# -*- coding: utf-8 -*- 

class Rules:
    TotalRoles = 13
    (Reserved, Thief, Wolves, Humen, Witch, Cupid, Predict, \
    Guard, Hybird, Hunter, President, Idiot, Girl) = range(TotalRoles)
    
    FirstNight = [Thief, Cupid, Guard, Wolves, Predict, Witch, Hunter]
    Night = [Guard, Predict, Wolves, Witch]

    MinUsers = 6
    MaxUsers = 18

class Camps:
    TotalCamps = 5
    (Undecided, Wolves, Gods, Humen, Wolfman) = range(TotalCamps)

class LiveStates:
    TotalLiveStates = 7
    (Undead, Voted, Killed, Poisoned, Couple, Huntered, Godskill) = range(TotalLiveStates)
