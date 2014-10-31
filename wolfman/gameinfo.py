# -*- coding: utf-8 -*- 

from role import *
#g for global

gtotalrole = 13
gturnnum = 0
gtotaluser = 0

#role id
(RReserved, RThief, RWolves, RHumen, RWitch, RCupid, RPredict, \
 RGuard, RHybird, RHunter, RPresident, RIdiot, RGirl) = range(gtotalrole)

#camp
(CUndecided, CWolves, CGods, CHumen, CWolfman) = range(5)

#role number of each role
grolelist = []

#role of each user
gtotaluser = []

def gameinit(totaluser):
    gtotaluser = totaluser
    grolelist = [0 for i in range(totalrole)]
    guserlist = [0 for i in range(totaluser)]


