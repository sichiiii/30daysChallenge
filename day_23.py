#https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python   руки разминал
def disemvowel(string_):
    string_ = string_.replace('a', '')
    string_ = string_.replace('e', '')
    string_ = string_.replace('i', '')
    string_ = string_.replace('o', '')
    string_ = string_.replace('u', '')
    string_ = string_.replace('A', '')
    string_ = string_.replace('E', '')
    string_ = string_.replace('I', '')
    string_ = string_.replace('O', '')
    string_ = string_.replace('U', '')
    return string_
  
#https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
def high_and_low(numbers):
    max, min = -100000, 1000000
    for i in numbers.split(' '):
        if int(i) > max:
            max = int(i)
        if int(i) < min:
            min = int(i)
    return str(max) + ' ' + str(min)
  
#https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
def digital_root(n):
    sum = n
    buffer = 10
    while n > 9:
        sum = 0
        while (n > 0):
            sum = sum + (n % 10)
            n = n//10
        n = sum
    return sum
  
#https://www.codewars.com/kata/56747fd5cb988479af000028/train/python
def get_middle(s):
    if len(s) < 3:
        return s
    if len(s) % 2 == 0:
        return s[len(s)-len(s)//2-1] + s[len(s)-len(s)//2] 
    else:
        return s[len(s)-len(s)//2-1]
  
#https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python
def descending_order(num):
    result = ''
    for i in sorted(list(str(num)), reverse=True):
        result+=i
    return int(result)

#https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/solutions/python
def find_short(s):
    min = len(s)
    for i in s.split(' '):
        if len(i) < min:
            min = len(i)
    return min
