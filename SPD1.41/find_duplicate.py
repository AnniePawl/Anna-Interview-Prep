# Given array of n numbers that are all unique except one duplicate, find duplicate 

# .count() method list comprehension 
# Time complexity O(n) - not that efficient b/c iterating over all elements to check count
def find_duplicate_count(nums):
  return [num for num in nums if nums.count(num) >1][0]

# .index() method 
# Time complexity O(nlogn)
def find_duplicate_index(nums):
  [nums[i] for i in range(len(nums)) if i == nums.index(nums[i])]


nums = [1,2,3,4,5,6,7,8,9,3]
print(find_duplicate_count(nums)) # 3 
print(find_duplicate_index(nums)) # 3 