#https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python
def is_valid_walk(walk):
    result = {'s' : 0, 'w' : 0}
    if len(walk) == 10:
        for i in walk:
            if i == 'n':
                result['s']-=1
            if i == 's':
                result['s']+=1
            if i == 'e':
                result['w']-=1
            if i == 'w':
                result['w']+=1
        return result['s'] == 0 and result['w'] == 0
    return False
  
  #https://www.codewars.com/kata/53368a47e38700bd8300030d/train/python
  def namelist(names):
    if names == []:
        return ''
    if len(names) == 1:
        return names[0]['name']
    if len(names) == 2:
        result = names[0]['name'] + " & " + names[1]['name']
        return result
    result = names[0]['name']
    for i in range(1 , len(names)):
        if i == len(names)-1:
            result+=' & '
            result+=names[i]['name']
            return result
        result+=', '
        result+=names[i]['name']

  #https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/python
def solution(n):
    total = n
    result = ''

    while (total > 0):
        while (total >= 1000):
            result += 'M'
            total -= 1000
        while (total >= 500 and total < 1000):
            if (total >= 900):
                result += 'CM'
                total -= 900
            elif (total >= 800 and total < 900):   
                result += 'DCCC'
                total -= 800
            elif (total >= 700 and total < 800):
                result += 'DCC'
                total -= 700
            elif (total >= 600 and total < 700):  
                result += 'DC'
                total -= 600   
            else:    
                result += 'D'
                total -= 500
        while (total >= 100 and total < 500):
            if (total >= 400):
                result += 'CD'
                total -= 400
            elif (total >= 300 and total < 400):
                result += 'CCC'
                total -= 300
            elif (total >= 200 and total < 300):
                result += 'CC'
                total -= 200
            else:
                result += 'C'
                total -= 100
        while (total >= 50 and total < 100):
            if (total >= 90 and total < 100):
                result += 'XC'
                total -= 90
            elif (total >= 80 and total < 90):
                result += 'LXXX'
                total -= 80
            elif (total >= 70 and total < 80):
                result += 'LXX'
                total -= 70
            elif (total >= 60 and total < 70):
                result += 'LX'
                total -= 60
            else:
                result += 'L'
                total -= 50
        while (total >= 10 and total < 50):
            if (total >= 40 and total < 50):
                result += 'XL'
                total -= 40
            elif (total >= 30 and total < 40):
                result += 'XXX'
                total -= 30
            elif (total >= 20 and total < 30):
                result += 'XX'
                total -= 20
            else:
                result += 'X'
                total -= 10
        while (total >= 5 and total < 10):
            if (total == 9):
                result += 'IX'
                total -= 9
            elif (total == 8):
                result += 'VIII'
                total -= 8
            elif (total == 7):
                result += 'VII'
                total -= 7
            elif (total == 6):
                result += 'VI'
                total -= 6
            else:
                result += 'V'
                total -= 5
        while (total >= 1 and total < 5):
            if (total == 4):
                result += 'IV'
                total -= 4
            elif (total == 3):
                result += 'III'
                total -= 3
            elif (total == 2):
                result += 'II'
                total -= 2
            else:
                result += 'I'
                total -= 1
            
    return result 
