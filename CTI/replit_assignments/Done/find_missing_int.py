# Given unsorted int array, find first missing positive integer 
# Algorithm should run in O(n)time- so no sorting 

def find_pos(integers):
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


print(find_pos([1,2,0])) # 3
print(find_pos([1,3,4,5])) # 2
print(find_pos([3,4,-1,1])) # 2
print(find_pos([-8,-7,-6])) # 1

# CTI SOLUTION 
def first_missing_positive_integer(integers):

  found_integers = []
  first_missing_integer = None
  for integer in integers:
    if integer < 0:
      continue
    if integer + 1 > (len(found_integers)):
      extension_length = integer - len(found_integers) + 1
      found_integers.extend([False] * extension_length)
    found_integers[integer] = True
  for position in range(1,len(found_integers)):
    if found_integers[position] == False:
      first_missing_integer = position
      break
  if first_missing_integer != None:
    return first_missing_integer
  else:
    return max(len(found_integers),1)


# def find_pos(nums):
#   found_ints = []
#   for num in nums:
#     if num < 0:
#       continue
#     if num + 1 > len(found_ints):
#       extend_size = num - len(found_ints) + 1
#       found_ints.extend([False]* extend_size)
#     found_ints[num] = True

#   missing_int = 1 
#   for position in range(1, len(found_ints)):
#     if found_ints[position] == False:
#       missing_int = position
#   if missing_int == 0 and len(found_ints) ==0 :
#     return 1 
#   elif missing_int == 0 and len(found_ints) >0:
    
# return found_ints
