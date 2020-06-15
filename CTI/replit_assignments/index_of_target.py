# Given array of sorted ints, return starting and ending index or target num. If target not found, return [-1,-1]

def index_of_target(arr, target):
  if arr.count(target) == 0:
    return [-1,-1]
  else:
    return [arr.index(target), (len(arr)-1) - arr[::-1].index(target)]


print(index_of_target([5,7,7,8,8,10], 8)) # [3,4]
print(index_of_target([5,7,7,8,8,10], 11)) # [-1,-1]