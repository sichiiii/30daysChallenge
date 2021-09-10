#https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python
def is_valid_walk(walk):
    result = {'s' : 0, 'w' : 0}
    if len(walk) == 10:
        for i in walk:
            if i == 'n':
                result['s']-=1
            if i == 's':
                result['s']+=1
            if i == 'e':
                result['w']-=1
            if i == 'w':
                result['w']+=1
        return result['s'] == 0 and result['w'] == 0
    return False
  
  #https://www.codewars.com/kata/53368a47e38700bd8300030d/train/python
  def namelist(names):
    if names == []:
        return ''
    if len(names) == 1:
        return names[0]['name']
    if len(names) == 2:
        result = names[0]['name'] + " & " + names[1]['name']
        return result
    result = names[0]['name']
    for i in range(1 , len(names)):
        if i == len(names)-1:
            result+=' & '
            result+=names[i]['name']
            return result
        result+=', '
        result+=names[i]['name']
