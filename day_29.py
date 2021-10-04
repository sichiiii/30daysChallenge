#https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python
def binary_array_to_number(arr):
    bin_num = ''
    for i in arr:
        bin_num+=str(i)
    return int(bin_num, 2)
