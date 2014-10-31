from gameinfo import *
from gameprompt import *

class AbsRole:
    users = []
    death = Undead
    role = Reserved
    ramp = Undecided
    
    def __init__(self, userlist):
        for i in range(len(userlist)):
            self.users.append(userlist[i])

    #first night act
    def fnact(self):
        return;

    #normal night act
    def nact(self):
        return

    def death(self, reason, turn):
        return

    def print(self):
        return

class RoleWolves(AbsRole):
    role = Wolves
    
    def fnact(self):
        setusers(self.hasRole(Wolves), Wolves)

    def nact(self):
        wolfkill(achooseuser())

    def print(self):
        print(self.users)
