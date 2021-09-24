#https://www.codewars.com/kata/6071ef9cbe6ec400228d9531/train/python
def calculator(txt):
    buff_arr = txt.split(' ')
    if '+' in buff_arr:
        count = len(buff_arr[0]) + len(buff_arr[2])
    elif '-' in buff_arr:
        count = len(buff_arr[0]) - len(buff_arr[2])
    elif '*' in buff_arr:
        count = len(buff_arr[0]) * len(buff_arr[2])
    elif '//' in buff_arr:
        count = len(buff_arr[0]) // len(buff_arr[2])
    result = ''
    for i in range(0, count):
        result += '.'
    return result

#https://www.codewars.com/kata/60f94b4c8b940b0038f5e237/train/python
def boom_intensity(n):
    if n == 1:
        return 'boom'
    result = 'B'
    for i in range(n):
        result += 'o'
    result +='m'
    if n % 2 == 0:
        result += '!'
    if n % 5 == 0:
        result = result.upper()
    return result
