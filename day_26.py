#https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python
def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        if pin.isdigit():
            return True
    return False
  
 #https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
 def pig_it(text):
    result = ''
    for i in text.split(' '):
        if len(i) > -1 and i != '?' and i != '!':
            result+=i[1:]+i[0]+'ay '
        else:
            result+=i
    if '!' in text:
        result += '!'
    if '?' in text:
        result += '?'
    return result[:-1] 
