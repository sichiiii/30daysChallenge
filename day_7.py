#https://www.codewars.com/kata/602db3215c22df000e8544f0/train/python
def two_are_positive(a, b, c):
    if (a >= 0 and b > 0 and c <= 0) or (a > 0 and b <= 0 and c > 0) or (a <= 0 and b > 0 and c > 0):
        return True
    else:
        return False
