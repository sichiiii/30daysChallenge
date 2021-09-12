#https://www.codewars.com/kata/5fb856190d5230001d48d721/train/python
def pentagonal(n):
    if n >= 1:
        return (5*(n**2)-5*n+2)//2
    return -1
