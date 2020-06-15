# Given unsorted int array, find first missing positive integer 
# Algorithm should run in O(n)time- so no sorting 

def find_pos(nums):
  found_ints = []
  for num in nums:
    if num < 0:
      continue
    if num + 1 > len(found_ints):
      extend_size = num - len(found_ints) + 1
      found_ints.extend([False]* extend_size)
    found_ints[num] = True

  missing_int = 1 
  for position in range(1, len(found_ints)):
    if found_ints[position] == False:
      missing_int = position
  if missing_int == 0 and len(found_ints) ==0 :
    return 1 
  elif missing_int == 0 and len(found_ints) >0:
    
  return found_ints




  
  

print(find_pos([1,2,0])) # 3
print(find_pos([3,4,-1,1])) # 2
print(find_pos([-8,-7,-6])) # 1