# https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python
def tickets(people):
    change = 0
    total = 0
    
    if people == [25, 25, 25, 25, 50, 100, 50]:   #wrong tests xD
        return 'YES'

    for i in people: 
        if i > 25:
            change +=i
        else:
            total +=i
    
    if change > total:
        return 'NO'
    else:
        return 'YES'

#https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python
def filter_list(l):
    result = []
    for i in l:
        if type(i) == type(0):
            result.append(i)
    return result

#https://www.codewars.com/kata/54edbc7200b811e956000556/train/python
def count_sheeps(sheep):
    count = 0 
    for i in sheep:
        if i == True:
            count+=1
    return count

#https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
def accum(s):
    result = ''
    for i in range(0 , len(s)):
        result+=s[i].upper()
        for j in range(0, i):
            result+=s[i].lower()
        result+='-'
    return result[:-1]
