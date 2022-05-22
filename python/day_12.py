#https://www.codewars.com/kata/5fb856190d5230001d48d721/train/python
def pentagonal(n):
    if n >= 1:
        return (5*(n**2)-5*n+2)//2
    return -1

#https://www.codewars.com/kata/5f6787948a3830002fc40077/train/python      #trash
def expand_usernames(data): 
    result = []
    buffer = []
    for i in range(0, len(data)):
        spl = data[i][0].split(',')
        if len(spl) > 0:
            for j in spl:
                #j = j.replace(' ', '')
                if j != '' and j != ' ' and j != '   ':
                    if j[0] == ' ':
                        j = j[1:]
                    if j[-1] == ' ':
                        j = j[:-1]
                    if j[-1] == ' ':
                        j = j[:-1]
                    buffer = [j, data[i][1]] 
                    result.append(buffer)
                    buffer = []
        else:
            result.append(data[i])
