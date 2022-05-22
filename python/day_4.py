#https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3/solutions/python
def unpack(iter):
    return [e for e in iter]

def find_uniq(arr):
    # lst = [''.join(sorted([*set(s.strip().lower())])) for s in arr] # Python 3.5
    lst = [''.join(sorted(unpack(set(s.strip().lower())))) for s in arr]
    a, b = set(lst)
    return arr[lst.index(a)] if lst.count(a) == 1 else arr[lst.index(b)]
  
  
#thanks to SeungUkLee
