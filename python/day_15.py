#https://www.codewars.com/kata/521ef596c106a935c0000519/train/python
def prime(n):
    result = []
    if n == 2:
        return [2]
    for i in range(2, n+1):
        if (i == 1):
            continue
        flag = 1
        for j in range(2, i // 2 + 1):
            if (i % j == 0):
                flag = 0
                break
        if (flag == 1):
            result.append(i)
    return result
