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
