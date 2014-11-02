# -*- coding: utf-8 -*- 
userlist = []
(ID, Total, Turn) = range(3)

def setuserlist() :
    maxname = 0
    for i in range(100) :
        username = input("用户" + str(i + 1) + "姓名:")
        if username == "b":
            break
        if len(username) > maxname:
            maxname = len(username)
        score = [username, 0, []]
        userlist.append(score)     
    printscore()
    return maxname

def printscore():
    print("\n积分板:")
    maxname = 7
    maxscore = 6
    for user in userlist:
        output = user[ID].ljust(maxname + 1)
        output += str(user[Total]).ljust(maxscore + 1)
        for score in user[Turn]:
            output += str(score).ljust(maxscore + 1)
        print(output)
    print("\n")

def addscore(uid, score):
    userlist[uid][Total] += score
    userlist[uid][Turn].append(score)    
            
def clean():
    for user in userlist:
        user[Total] = 0
        user[Turn] = [0]
    printscore()       

def msgrecv():
    uid = 0
    while (True) :
        username = userlist[uid][ID]
        inmsg = input(username + " 本轮积分: ")
        if inmsg == "c":
            clean()
            uid = 0
            continue
        elif inmsg == "s":
            printscore()

        if not type(inmsg) == int and not inmsg.isdigit() :
            continue
        addscore(uid, int(inmsg))
        uid += 1
        if uid == len(userlist):
            uid = 0
            printscore()                
    return

maxnamelen = setuserlist()
msgrecv()
printscore()

