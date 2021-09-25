#https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python
def count_bits(n):
    result = 0
    arr = list(bin(n))
    for i in range(2, len(arr)):
        if arr[i] == '1':
            result+=1
    return result
