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