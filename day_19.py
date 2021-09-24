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
