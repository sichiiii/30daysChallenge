#https://www.codewars.com/kata/5262119038c0985a5b00029f/train/python
def is_prime(n):
    if n <= 0 or n == 1:
        return False
    i = 2
    while (i <= n ** 0.5):
        if n % i == 0:
            return False
        i += 1
    return True
