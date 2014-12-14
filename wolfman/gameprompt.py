# -*- coding: utf-8 -*- 
from getinput import *
from rule import *
from check import *
from usercontrol import *

rolename = ["未定", "盗贼", "狼人", "普通村名", "女巫", "丘比特", "预言家", \
            "守卫", "混血儿", "猎人", "村长", "白痴", "小女孩"]
livename = ["生存", "票死", "狼人咬死", "女巫毒死", "情侣带死", "猎人带走"]

campname = ["未定", "狼人", "神", "普通村民", "人狼"]

ChineseLanguage = ["启用%s", "分发身份卡", "玩家人数建议 %d-%d 人", "情侣", \
        "是否启用%s", "%s请睁眼", "%s请闭眼", "天黑请闭眼", \
        "天亮了", "设置玩家人数", "请输入%s号码, 输入 0 表示没有该角色", "请输入情侣%d号码", \
        "该用户已有角色", "记住盗贼身份，请在之后输入", "%d 号和 %d 号是情侣", "本局没有情侣", \
        "请选择一名玩家, 输入 0 表示放弃", "%d 号玩家%s是狼人", "不", "今天晚上 %d 号玩家死了，你是否要使用解药", \
        "你是否要使用毒药， 输入 0 表示放弃使用", "%s 号死亡，死左发言", "竞选警长", "今晚被票死的是",
        "情侣请睁眼，互相认识一下", "丘比特请指定情侣", "角色是：%s", "阵营是：%s", \
        "存活状态：%s", "竞选成功的是", "玩家%d: 角色:%s, 生存:%s, 阵营:%s"]


(SActive, SDispatch, SNumError, SCouple, \
        SIsActive, SOpenEye, SCloseEye, SAllCloseEye, \
        SAllOpenEye, SSetPlayerNum, SUserRoleInput, SCoupleInput, \
        SHadRole, SThiefRole, SABisCouple, SNoCouple, \
        SChooseOneUser, SIsWolf, SNo, SWitchSave, \
        SWitchPoison, SDeathNight, SForChief, SVoteDeath, \
        SCoupleOpenEye, SCoupleSetting, SRole, SCamp, \
        SLiveState, SWinChief, SUserInfo) = range(31)


l = ChineseLanguage

def printNormal(prompt):
    print(prompt)

class Prompt:
    def normal(prompt):
        printNormal(prompt)

    def warning(prompt):
        Prompt.normal(prompt)

    def consoleLine():
        Prompt.normal("=========================")

    def help():
        Prompt.consoleLine()
        Prompt.normal("输入 \"i\" 获取所有人信息")
        Prompt.normal("输入 \"l\" 获取存活玩家信息")
        Prompt.normal("输入 \"k 3\" 杀死3号玩家")
        Prompt.normal("输入 \"a 3\" 救起3号玩家")
        Prompt.normal("输入 \"c 1 2\" 设置1号2号玩家为情侣")
        Prompt.normal("输入 \"o\" 获取所有角色的角色号")
        Prompt.normal("输入 \"r 3 2\" 设置3号玩家的角色为2")
        Prompt.consoleLine()

    def allUserInfo():
        i = 1
        Prompt.consoleLine()
        for user in usercontrol.userlist[1:]:
            s = l[SUserInfo] % (i, rolename[user.role], livename[user.livestate], campname[user.camp])
            Prompt.normal(s)
            i += 1
        Prompt.consoleLine()
        
    def thiefNight():
        Prompt.normal(l[SThiefRole])

    def activeRole(roleid, active):
        if active:
            Prompt.normal(l[SActive] % (rolename[roleid]))
            
    def dispatch():
        Prompt.normal(l[SDispatch])

    def isActive(roleid):
        Prompt.normal(l[SIsActive] % rolename[roleid])

    def showCouple(u1, u2):
        Prompt.normal(l[SABisCouple] % (u1, u2))

    def noCouple():
        Prompt.normal(l[SNoCouple])

    def isWolf(uid, iswolf):
        if iswolf:
            Prompt.normal(l[SIsWolf] % (uid, ""))
        else:
            Prompt.normal(l[SIsWolf] % (uid, l[SNo]))

    def warningPlayerNum():
        Prompt.normal(l[SNumError])

    def warningHadRole(roleid):
        Prompt.normal(l[SHadRole] % rolename[roleid])

        

    
class GodSays:
    def normal(prompt):
        printNormal("\n>>>" +(prompt))

    def openEye(roleid):
        GodSays.normal(l[SOpenEye] % (rolename[roleid]))
    
    def closeEye(roleid):
        GodSays.normal(l[SCloseEye] % (rolename[roleid]))

    def coupleMade():
        GodSays.normal(l[SCoupleSetting])
    
    def openEyeCouple():
        GodSays.normal(l[SCoupleOpenEye])
    
    def closeEyeCouple():
        GodSays.normal(l[SCloseEye] % l[SCouple])
    
    def closeEyeAll():
        GodSays.normal(l[SAllCloseEye])
    
    def openEyeAll():
        GodSays.normal(l[SAllOpenEye])
        
    def morning(deathlist):
        if len(deathlist) == 0:
            printGodSay(l[SSafenight])
        else:
            printGodSay(str(deathlist) + l[SDeathNight])
            
    def forChief():
        return GodSays.normal(l[SForChief])

def notcheck(n):
    return True

class Ask:
    def hasThief():
        return Get.bool(l[SHasThief])
    
    def useSave(u1):
        return Get.bool(l[SWitchSave] % u1)

    def normal(prompt, check = notcheck):
        i = 0
        while True:
            i = Get.raw(prompt)
            if i == "h":
                Prompt.help()
            elif i == "i":
                Prompt.allUserInfo()

            elif not type(i) is int and not i.isdigit():
                continue
            else:
                i = int(i)
                if check(i):
                    break
        return i
    
    
    
    def setUserRole(roleid, check, userseq = 0):
        if userseq == 0:
            return Ask.normal(l[SUserRoleInput] % (rolename[roleid]), check)
        else:
            return Ask.normal(l[SUserRoleInput] % (rolename[roleid] + str(userseq)), check)
    
    def playerNums(check):
        return Ask.normal(l[SSetPlayerNum], check)
    
    def setCouple(coupleid, check):
        return Ask.normal(l[SCoupleInput] % (coupleid), check)
    
    def chooseUser(check):
        return Ask.normal(l[SChooseOneUser], check)
    
    def usePoison(check):
        return Ask.normal(l[SWitchPoison], check)
    
    def userVoted(check):
        return Ask.normal(l[SVoteDeath], check)
    
    def winChief(check):
        return Ask.normal(l[SWinChief], check)
