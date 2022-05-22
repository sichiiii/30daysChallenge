#https://www.codewars.com/kata/57d14a9d95497e9912000267/train/python
def bath(string,bath):
    return  len(bath) - 2 - len(string) < 0

#https://www.codewars.com/kata/5e2456b1c4d2810023bb14e2/train/python
def which_pizza(d1,price1,d2,price2):
    if d1**2 / price1 < d2**2 / price2:
        return d2
    else:
        return d1

#https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python
def duplicate_count(text):
    count = 0
    my_dict = {i:list(text.lower()).count(i) for i in list(text.lower())}
    for i in my_dict.values():
        if i > 1:
            count+=1 
    return count
