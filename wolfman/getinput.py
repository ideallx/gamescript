# -*- coding: utf-8 -*- 

class Get:
    def num(prompt, shouldin):
        s = ""
        while True:
            s = input(prompt + ": ")
            if not type(s) is int and not s.isdigit():
                continue
            elif not int(s) in shouldin:
                continue
            else:
                return int(s)
    
    def bool(prompt):
        while True:
            s = input(prompt + "(y/n): ")
            if s == 'y':
                return True
            elif s == 'n':
                return False


