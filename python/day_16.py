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
    
    
#https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
def move_zeros(array):
    count = 0
    for i in array:
        if i == 0:
            count+=1
    for i in range(0, count):
        array.remove(0)
        array.append(0)
    return array
