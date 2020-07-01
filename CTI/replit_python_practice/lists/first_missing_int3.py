# Given an unsorted int, find first missing postiive num 
# Should run in O(n)  - so no sort
# Use as much space as you need

def first_missing(a):
  flag_array = [0 for x in range(len(a)+1)]
  for num in a:
    if num < 0:
      pass 
    else:
      if num >= len(flag_array):
        flag_array.extend([0 for x in range(num)])
      flag_array[num] = 1


  for i in range(1,len(flag_array)):
    if flag_array[i] == 0:
      return i


print(first_missing([0, 2, 1])) # 3
print(first_missing([-1,4, 1,3])) # 2
print(first_missing([-8, -9, -6])) # 1
print(first_missing([4, 2, 2, 3, 5, 1, 8, 7] )) # 6