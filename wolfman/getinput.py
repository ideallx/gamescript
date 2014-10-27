# -*- coding: utf-8 -*- 

def getnum(prompt):
    s = input(prompt + ": ")
    if not type(s) is int and not s.isdigit():
        return getnum(prompt)
    return int(s)
    
def getbool(prompt):
    s = input(prompt + "(y/n): ")
    if s == 'y':
        return True
    elif s == 'n':
        return False
    else:
        return getbool(prompt)
