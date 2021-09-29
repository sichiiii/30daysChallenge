#https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python
def to_jaden_case(string):
    result = ''
    for i in string.split(' '):
        result+=i[0].upper() + i[1:] + ' '
    return result[:-1]
  
#https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python
def find_outlier(integers):
    if len(integers) < 2:
        return integers[1]
    else:
        odd = 0
        notOdd = 0
        for i in range(0, 3):
            if integers[i] % 2 == 0:
                odd+=1
            else:
                notOdd+=1
        if odd > notOdd:
            for i in integers:
                if i % 2 != 0:
                    return i
        else:
            for i in integers:
                if i % 2 == 0:
                    return i
                  
#https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python             
def is_isogram(string):
    access = True
    letters = []
    for i in list(string):
        if i.lower() in letters:
            return False
        letters.append(i.lower())
    return access  
  
#https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python
def alphabet_position(text):
    result = ''
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in text.split(' '):
        for j in i:
            if j.lower() in alph:
                result+=str(alph.index(j.lower())+1) + ' '
    return result[:-1]

#https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python
def maskify(cc):
    if len(cc) > 3:
        return '#' * (len(cc)-4) + cc[-4:]
    return cc

