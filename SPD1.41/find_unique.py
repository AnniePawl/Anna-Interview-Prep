# Given array of all duplicates except 1 unique value, find unique value

# .count() method 
def find_unique(nums):
  return [num for num in nums if nums.count(num) < 2][0]

# set method 



nums = [1,1,2,2,3,3,4,5,5] 
print(find_unique(nums)) # 4 
print(find_unique_set(nums)) # 4 