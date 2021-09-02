#https://www.codewars.com/kata/5287e858c6b5a9678200083c/solutions/python

def narcissistic(value):
    poweredNum = 0
    for i in str(value):
        poweredNum += int(i)**len(str(value))
    if poweredNum == value:
        return True
    else:
        return False
