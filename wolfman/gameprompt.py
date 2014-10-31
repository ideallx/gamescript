# -*- coding: utf-8 -*- 
from getinput import *
from gameinfo import *

# pXXXX  print
# aXXXX  ask
# gXXXX  god say
# fXXXX  format
# SXXXX  prompt

rolename = ["角色未定义", "盗贼", "狼人", "普通村名", "女巫", "丘比特", "预言家", \
            "守卫", "混血儿", "猎人", "村长", "白痴", "小女孩"]

SCouple = "情侣"
SActive = "启用"
SHasThief = "是否启用盗贼"
SOpenEye = "请睁眼"
SCloseEye = "请闭眼"
SAllCloseEye = "天黑请闭眼"
SAllOpenEye = "天亮了"
SDispatch = "分发身份卡"
SSetPlayerNum = "设置玩家人数"
SNumError = "玩家人数建议 6-18 人"
SUserRoleInput = "请输入%s号码, 输入 0 表示没有该角色"
SCoupleInput = "请输入情侣%d号码"
SHadRole = "该用户已有角色"
SThiefRole = "记住盗贼身份，请在之后输入"
SABisCouple = "%d 号和 %d 号是情侣"
SNoCouple = "本局没有情侣"
SChooseOneUser = "请选择一名玩家, 输入 0 表示放弃"
SIsWolf = "%d 号玩家%s是狼人"
SNo = "不"
SWitchSave = "今天晚上 %d 号玩家死了，你是否要使用解药"
SWitchPoison = "你是否要使用毒药， 输入 0 表示放弃使用"
SDeathNight = "号死亡，死左发言"
SForChief = "竞选警长"
SVoteDeath = "今晚被票死的是"

def phelp():
    print("输入 \"i\" 获取所有人信息")
    print("输入 \"l\" 获取存活玩家信息")
    print("输入 \"k 3\" 杀死3号玩家")
    print("输入 \"a 3\" 救起3号玩家")
    print("输入 \"c 1 2\" 设置1号2号玩家为情侣")
    print("输入 \"o\" 获取所有角色的角色号")
    print("输入 \"r 3 2\" 设置3号玩家的角色为2")
    

def printNormal(prompt):
    print(prompt)

def printGodSay(prompt):
    printNormal(fgodsay(prompt))



def fgodsay(prompt):
    return "\n>>>" + prompt


def pactiverole(roleid, active):
    if active:
        printNormal(SActive + rolename[roleid])

def prolenum(roleid, rolenum):
    printNormal(str(rolenum) + " " + rolename[roleid])

def pdispatchrole():
    printNormal(SDispatch)

def pplayernumerror():
    printNormal(SNumError)

def puserhadrole(roleid):
    printNormal(SHadRole + rolename[roleid])

def pthiefrole():
    printNormal(SThiefRole)

def piscouple(c1, c2):
    printNormal(SABisCouple %(c1, c2))

def pnocouple():
    printNormal(SNoCouple)

def piswolf(uid, iswolf):
    if iswolf:
        printNormal(SIsWolf %(uid, ""))
    else:
        printNormal(SIsWolf %(uid, SNo))

def faskNum(prompt, check):
    i = 0
    while True:
        i = getnum(prompt)
        if check(i):
            break
    return i

def aforchief():
    return input(SForChief)
    
def ahasthief():
    return getbool(SHasThief)

def ausesave(u1):
    return getbool(SWitchSave % u1)


def asetuserrole(roleid, check, userseq = 0):
    if userseq == 0:
        return faskNum(SUserRoleInput % rolename[roleid])
    else:
        return faskNum(SUserRoleInput % (rolename[roleid] + str(userseq))

def aplayernum(check):
    return faskNum(SSetPlayerNum, check)

def asetcouple(coupleid, check):
    return faskNum(SCoupleInput % coupleid, check)

def achooseuser(check):
    return faskNum(SChooseOneUser, check)

def ausepoison(check):
    return faskNum(SWitchPoison, check)

def auservoted(check):
    return faskNum(SVoteDeath, check)



def gmorning(deathlist):
    if len(deathlist) == 0:
        printGodSay(SSafenight)
    else:
        printGodSay(str(deathlist) + SDeathNight)

def gopeneye(roleid):
    printGodSay(rolename[roleid] + SOpenEye)

def gcloseeye(roleid):
    printGodSay(rolename[roleid] + SCloseEye)

def gcoupleopeneye():
    printGodSay(SCouple + SOpenEye)

def gcouplecloseeye():
    printGodSay(SCouple + SCloseEye)

def gallcloseeye():
    printGodSay(SAllCloseEye)

def gallopeneye():
    printGodSay(SAllOpenEye)
    
