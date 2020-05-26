#  Gven array of n ints, find how many times you have to add smallest numbers in array until they become larger of equal to k 

def min_steps(arr, k):
  arr = sorted(arr)
  sum = 0
  count = 0
  for i in range(len(arr)):
    sum += arr[i]
    if sum < k:
      count +=1
    else:
      break
  return count




print(min_steps([1,10,12,9,2,3], 6)) # 2
print(min_steps([10,9,9,8], 17)) # 1
print(min_steps([8,9,10,4,2], 23)) # 3
print(min_steps([4,6,3], 2)) # 0