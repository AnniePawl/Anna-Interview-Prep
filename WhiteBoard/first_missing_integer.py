# Given an unsorted integer array, find first missing positive integer 
# Algorithm should run in O(n) time, so NO sorting 
# Algorithm should have 0(n) extra space 

def first_missing(integers):
  flag_array = [0 for x in range(len(integers)+1)]
  for num in integers:
    if num < 0:
      pass 
    else:
      if num >= len(flag_array):
        flag_array.extend([0 for x in range(num)])
      flag_array[num] = 1

  for i in range(1,len(flag_array)):
    if flag_array[i] == 0:
      return i

print(first_missing([1,2,0])) # 3
print(first_missing([3,4,-1,1] )) # 2
print(first_missing([-8, -7, -6])) # 1
print(first_missing([3,4,5,6,8])) # 7



def first_missing2(ints):
  


print(first_missing2([7,-2,3,1,2,20,-5])) # 4
# print(first_missing2([1,2,0])) # 3
# print(first_missing2([3,4,-1,1] )) # 2
# print(first_missing2([-8, -7, -6])) # 1
# print(first_missing2([3,4,5,6,8])) # 7
