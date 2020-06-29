# Given sorted array and target value, return index of target is found. If not, return index where it should be if inserted in order. No duplicates in array 

def find_index(arr, target):
  if target in arr: 
    return arr.index(target)
  else:
    if target > arr[-1]:
      return len(arr)
    if target < arr[0]:
      return 0 
    for i in range(len(arr)-1):
      if arr[i] < target and arr[i+1] > target:
        return i+1

def find_index2(arr,target):
  try:
    return arr.index(target)
  except:
    for i in range(len(arr)):
      if arr[i] - target > 0:
        return i 
    else:
      return len(arr)
      


print(find_index([1,3,5,6], 5)) # 2
print(find_index([1,3,5,6], 2)) # 1
print(find_index([1,3,5,6], 7)) # 4
print(find_index([1,3,5,6], 0)) # 0


print("find index 2")
print(find_index2([1,3,5,6], 5)) # 2
print(find_index2([1,3,5,6], 2)) # 1
print(find_index2([1,3,5,6], 7)) # 4
print(find_index2([1,3,5,6], 0)) # 0

