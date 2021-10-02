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
