#https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python
def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds-hours*3600)//60
    seconds = seconds - hours * 3600 - minutes * 60
    result = ''
    if hours > 0:
        if hours < 10:
            result+='0'
        result += str(hours) + ':'
    else:
        result +='00:'
    if minutes > 0:
        if minutes < 10:
            result+='0'
        result += str(minutes) + ':'
    else:
        result +='00:'
    if seconds < 10:
        result +='0'
    return result+str(seconds)
    
