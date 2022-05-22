#https://www.codewars.com/kata/5287e858c6b5a9678200083c/solutions/python
def narcissistic(value):
    poweredNum = 0
    for i in str(value):
        poweredNum += int(i)**len(str(value))
    if poweredNum == value:
        return True
    else:
        return False

#https://www.codewars.com/kata/551dd1f424b7a4cdae0001f0/train/python
def who_is_next(names, r):
    n = len(names)
    while r > n:
        r = (r - n + 1) >> 1
    return names[r - 1]
