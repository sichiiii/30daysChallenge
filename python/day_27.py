#https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/python
def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return [1,15,15]
    elif human_years == 2:
        return [2,24,24]
    else:
        result = [0,0,0]
        result[0]+=human_years
        result[1]+=24
        result[2]+=24
        for i in range(2, human_years):
            result[1]+=4
            result[2]+=5
    return result

#https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python
def dig_pow(n, p):
    buffer = 0
    count = p
    for i in str(n):
        buffer+=int(i)**count
        count+=1
    if buffer % n == 0:
        return buffer//n
    return -1
