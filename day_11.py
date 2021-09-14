#https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
def unique_in_order(iterable):
    result = []
    if iterable != '':
        result.append(iterable[0])
        for i in range(0, len(iterable)):
            if i > 0:
                if iterable[i] != iterable[i-1]:
                    result.append(iterable[i])
        return result
    return result
  
#https://www.codewars.com/kata/5f84327ac00bae002444d813/train/python
def match_words(acronym,words):
    result = {}
    for i in acronym:
        for j in range(0, len(words)):
            if words[j][0] == i:
                result[i] = words[j]
    return result


