#https://www.codewars.com/kata/5208fc3cb613bc725f000142/train/python    too easy
def solution(st, limit):
    if limit < len(st):
        return(st[:limit] + '...')
    return(st[:limit])

#https://www.codewars.com/kata/5264d2b162488dc400000001/train/python  
def spin_words(sentence):
    words = sentence.split()
    for i in range(0, len(words)):
        if len(words[i]) > 4:
            words[i] = words[i][::-1]
    return " ".join(words)
  
