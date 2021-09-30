#https://www.codewars.com/kata/57f5e7bd60d0a0cfd900032d/train/python
def missing_no(nums):
    for i in range(0, len(nums)+1):
        if i not in nums:
            return i
          
#https://www.codewars.com/kata/585d7d5adb20cf33cb000235/solutions/python
def find_uniq(arr):
    count_dict = {}
    for i in arr:
        if i not in count_dict:
            count_dict[i]=1
        else:
            count_dict[i]+=1
    for i in count_dict:
        if count_dict[i] == 1:
            return i
