#https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
def array_diff(a, b):
    expected = []
    for i in a:
        if i not in b:
            expected.append(i)
    return expected
  

#https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
import collections

def duplicate_encode(word):
    counts = dict(collections.Counter(word.lower()))
    result = ''
    for i in word.lower():        
        if counts[i] == 1:
            result += '('
        else:
            result += ')'
    return result
