nums = [1,2,3,4,5,6,7,8,9,10]
strs = ['anna', 'go', 'a', 'candle', 'to', 'butter', 'i']
tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# 1. Sum items in list 
def sum_list(nums):
  return sum(nums)

def sum_list2(nums):
  sum = 0 
  for num in nums:
    sum += num 
  return sum

print(sum_list(nums)) # 55s
print(sum_list2(nums)) # 55s

# 2. Multiply items in list 
def mult(nums):
  result = 1
  for num in nums:
    result *= num
  return result 

print(mult(nums)) # 3628800

# 3. Get largest num from a list 
def largest(nums):
  return max(nums)

def largest2(nums):
  largest = nums[0]
  for num in nums:
    if num > largest:
      largest = num
  return num

print(largest(nums)) # 10
print(largest2(nums)) # 10

# 4. Get min from list
def min(nums):
  return min(nums)

# 5. Count number of strings where len > 2
def count_strings(strs):
  count = 0 
  for item in strs:
    if len(item) > 2:
      count += 1
  return count

def count_strs2(strs):
  return sum(1 for str in strs if len(str) > 2)

print(count_strings(strs))
print(count_strs2(strs))

# 6. Given list of tuples, sort in increasing order by last item in each tuple 

def sort_tuples(tuples):
  return sorted(tuples, key = lambda x:x[1])

print(sort_tuples(tuples)) # [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# 7. Remove duplicates from a list 
def remove_dups(nums):
  new = []
  for num in nums:
    if num not in new:
      new.append(num)
  return new

def remove_dups2(nums):
  result = []
  [result.append(num) for num in nums if num not in result]
  return result

def remove_dups_set(nums):
  return list(set(nums))
  
print(remove_dups([1,1,2,3,4,4,5])) # 1,2,3,4,5
print(remove_dups2([1,1,2,3,4,4,5])) # 1,2,3,4,5
print(remove_dups_set([1,1,2,3,4,4,5])) # 1,2,3,4,5

# 8. Check if list is empty 
def empty(nums):
  if not nums:
    return 'list empty'
  return True

print(empty([])) # True
print(empty([1,2])) # False

# 9. Clone a list 
def clone(nums):
  return list(nums)

def clone2(nums):
  return nums.copy()  

print(clone(nums))
print(clone2(nums))

# 10. Return list of words longer than 3 
def longerthree(strs):
  new_list = [ ]
  for word in strs:
    if len(word) > 3:
      new_list.append(word)
  return new_list

print(longerthree(strs))

# 11. Return True if two lists have a common member 
def common(s1,s2):
  for item in s1:
    if item in s2:
      return True 
      break 
  return False

def common_set(a,b):
  a = set(a)
  b = set(b)
  if a & b:
    return True
  return False
  

print(common([1,2,3], [5,4,1])) # True 
print(common([1,2,3], [4,5,6])) # False 
print(common_set([1,2,3], [5,4,1])) # True 
print(common_set([1,2,3], [4,5,6])) # False 

# 12. Remove first and last elements from list 
def remove_first_last(list):
  list.pop(0)
  list.pop(-1)
  return list

# this didnt word for last index -1 ???
def remove_first_last2(list):
  list = [num for (i,num) in enumerate(list) if i not in (0,(-1))]
  return list 

print(remove_first_last([1,2,3,4])) # 2,3
print(remove_first_last2([1,2,3,4])) # 2,3

# 13. Generate 3*4*6* 3d array with * for each element
def threed():
  array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]
  print(array)

print(threed())

# 14 . Remove even numbers from a list 
def remove_evens(nums):
  for num in nums:
    if num % 2 == 0:
      nums.remove(num)
  return nums

def remove_evens2(nums):
  return [num for num in nums if num % 2 != 0]

print(remove_evens(nums))
print(remove_evens2(nums))

# 15. shuffle list. import shufft 

# 16. Print list squares from range 1,10
def squares():
  squares = [num**2 for num in range(1,10)]
  return squares

print(squares())

# 17. / 

# 18. Generate all permutations of a list 
# import intertools

# 19. Get difference betwenn 2 listss
def difference(l1,l2):
  # without set 
  print(l1+l2)
  return [num for num in l1 + l2 if num not in l1 or num not in l2]

def difference2(l1,l2):
  # using set
  diff1 = list(set(l1) - set(l2))
  diff2 = list(set(l2) - set(l1))
  return diff1+diff2

print(difference([1,2,3],[3,4,5])) # [1,2,4,5]
print(difference2([1,2,3],[3,4,5])) # [1,2,4,5]

# 20. Return each value in list and it's index
def ienum(nums):
  for i, num in enumerate(nums):
    print(i, num)

print(ienum([1,2,3]))

# 21. Convery list of chars into a string 
def char_str(chars):
  return ''.join(chars)

print(char_str(['a','n','n','a']))


# 22. Find index of a specific item in list 
def find_index(list, num):
  return list.index(num)

print(find_index([1,2,3,4], 4)) # 3

# 23. Combine multiple lists into one list 
# you can also import intertools and use .chain
def combine_lists(l):
  new_list= []
  for minilist in l:
    for item in minilist:
      new_list.append(item)

  return new_list

print(combine_lists([[1,2], [3,4], [5,6]])) # [1,2,3,4,5,6]
  

# 24. Append l2 to l1 
def appendlist(l1,l2):
  return l1 + l2

print(appendlist([1,2], [3,4]))

# 25. Randomly select item from list 
# import random 
# print(random.choice(list))

# Check if 2 lists are circularly simialr 

# 27. Find second smallest number in a list 
def second_smallest(l):
  # sort list and find item at 1st index  (only works if list doesnt have duplicates)
  # return sorted(l)[1]
  return sorted(list(set(l)))[1]

print(second_smallest([3,5,6,2,1,1])) # 2

# 28. Find second largest number in list 

# 29. Extract unique values from a list 
# Using dictionary
def unique_vals(nums):
  unique = []
  vals = {}
  for num in nums:
    if num in vals:
      vals[num] += num 
    else:
      vals[num] = 1
  for key, value in vals.items():
    if value == 1:
      unique.append(key)
  return unique

print(unique_vals([1,1,2,3,3,4])) # 2,4

# 30. Get frequeny of elements in a list 
# You can use counter from collections
def frequency(list):
  histo = {}
  for item in list:
    if item in histo:
      histo[item] += 1 
    else:
      histo[item] = 1 
  return histo

print(frequency([1,1,2,'two', 'two', 4, 'annas']))

# 31. Count number of elements in specified range 
def num_in_range(nums, min, max):
  count = 0
  for num in nums: 
    if num < max and num > min:
      count +=1 
  return count

print(num_in_range([10,20,30,40,40,70,80,99], 40,100))


# 32. Check if list contains sublist 
# See sublists.py

# 33. Generate all sublists of alist 
# see sublists.py