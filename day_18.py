#https://www.codewars.com/kata/5848565e273af816fb000449/train/python
def encrypt_this(text):
        result = ''
        for i in text.split():
            buffer = ''
            buffer+=str(ord(i[0]))
            for j in range(0, len(i)):
                new = ""
                temp = ""
                for j in range(len(i)):
                    if j == 0:
                        new += str(ord(i[j]))
                    elif j == 1:
                        temp = i[j]
                        new += i[-1]
                    elif j == len(i) - 1:
                        new += temp
                    else:
                        new += i[j]  
            result+=new
            result+=' '
        return result[:-1]

#https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
def likes(names):
    if names == []:
        result = 'no one'
    elif len(names) == 1:
        result = names[0]
    elif len(names) == 2:
        result = names[0] + ' and ' + names[1]
        return result+' like this'
    elif len(names) == 3:
        result = names[0] + ', ' + names[1] + ' and ' +names[2]
        return result+' like this'
    else:
        result = names[0] + ', ' + names[1] + ' and ' + str(len(names)-2) + ' others'
        return result+' like this' 
    return result+' likes this'
