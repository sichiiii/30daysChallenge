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
