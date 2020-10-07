# Given a list of nums, with all elements sorted in ascending order, determine and print number of distinct elements 

def distinct_elements(nums):
  nums_set = set(nums)
  return len(nums_set)



print(distinct_elements([1,2,2,3,3,3])) # 