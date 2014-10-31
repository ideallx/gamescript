from gameinfo import *
from gameprompt import *


#fXXX first nigth act
#nXXX night act

factlist = [actNull, fThief, fWolves, fHumen, fWitch, fCupid, fPredict, \
            fGuard, fHybird, fHunter, fPresident, fIdiot, fGirl]
nactlist = [actNull, nThief, nWolves, nHumen, nWitch, nCupid, nPredict, \
            nGuard, nHybird, nHunter, nPresident, nIdiot, nGirl]

def actNull():
    return

def setuser():
    while True:
        i = asetuserrole(roleid)
        if self.uc.setuser(i,  role):
            return
        else:
            puserhadrole(self.uc.userlist[i][Role])
                
def acthasrole(roleid)
    return rolelist[roleid]

def actnight(roleid):
    if not acthasrole:
        return;
    gopeneye(roleid)
    nactlist[roleid]()
    gcloseeye(roleid)
    

def actfirstnight(roleid):
    if not acthasrole:
        return;
    
    gopeneye(roleid)
    factlist[roleid]()
    nactlist[roleid]()
    gcloseeye(roleid)
        
def fThief():
    pthiefrole()

def nThief():
    actNull()

def fCupid():
    setuser(Cupid)

    u1 = asetcouple(1)
    u2 = asetcouple(2)
            
    if self.uc.setcouple(u1, u2):
        piscouple(u1, u2)
    else:
        pnocouple()
    #couple??

def nCupid():
    actNull()

def fWolves():
    setusers(self.hasRole(Wolves), Wolves)

def nWolves():
    uc.wolfkill(achooseuser())

def fPredict():
    setuser(Predict)

def nPredict():
    i = achooseuser()
    piswolf(i, self.uc.iswolf(i))

def fWitch():
    setuser(Witch)

def nWitch():
    b = ausesave(self.uc.killed)
    if b:
        self.uc.witchsave()

    i = ausepoison()
    uc.witchpoison(i)

def fHunter():
    self.setuser(Hunter)

def nHunter():
    actNull()
