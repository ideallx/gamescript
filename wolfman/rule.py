# -*- coding: utf-8 -*- 

class Roles:
    TotalRoles = 13
    (Reserved, Thief, Wolves, Humen, Witch, Cupid, Predict, \
    Guard, Hybird, Hunter, President, Idiot, Girl) = range(TotalRoles)
    
    TotalCamps = 5
    (Undecided, Wolves, Gods, Humen, Wolfman) = range(TotalCamps)

    Morning = [Thief, Cupid, Guard, Wolves, Predict, Witch, Hunter]

    Night = [Guard, Predict, Witch]

    MinUsers = 6
    MaxUsers = 18
