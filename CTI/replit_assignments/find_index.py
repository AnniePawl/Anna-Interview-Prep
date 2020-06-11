# Given sorted array and target value, return index of target is found. If not, return index where it should be if inserted in order. No duplicates in array 

def find_index(arr, target):
  if target in arr: 
    return arr.index(target)
  else:
    return arr.index(target-1) + 1

print(find_index([1,3,5,6], 5)) # 2
print(find_index([1,3,5,6], 2)) # 1
print(find_index([1,3,5,6], 7)) # 4
print(find_index([1,3,5,6], 0)) # 0