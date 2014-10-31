
totalrole = 13

#role id
(Reserved, Thief, Wolves, Humen, Witch, Cupid, Predict, \
 Guard, Hybird, Hunter, President, Idiot, Girl) = range(totalrole)

#userlist info
(Userid, Livestate, Role, Camp) = range(4)

#live state
(Undead, Vote, Wolfkill, Poisoned, Love, Gun) = range(6)

#camp
(Undecided, Wolves, Gods, Humen, Wolfman) = range(5)

#skilllist

rolelist = []
userlist = []
skilllist = []

def gameinit(totaluser):
    rolelist = [0 for i in range(totalrole)]
    userlist = [[str(i), Reserved, Undecided]
                for i in range(totaluser + 1)]
    
