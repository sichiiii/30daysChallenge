#https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004/train/python
def highest_rank(arr):
    most_freq = 0
    count = 0
    for i in arr:
        times = arr.count(i)
        if times > count:
            most_freq = i
            count = times
        elif times == count:
            if most_freq < i:
                most_freq = i
    return most_freq
