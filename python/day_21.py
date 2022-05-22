#https://www.codewars.com/kata/6098205ca76224000d62a2d0/train/python
# NO NUMBERS IN THE CODE!!!
def numbers_without_numbers():
    arr = ['z', 'f', 's', 't', 'fo', 'ft']
    result = ''
    result += str(arr.index('t')) + str(arr.index('s')) + str(arr.index('f')) + \
    str(arr.index('ft')) + str(arr.index('f')) + str(arr.index('fo')) + str(arr.index('t')) \
    + str(arr.index('s')) + str(arr.index('ft'))
    return int(result)     #xD
