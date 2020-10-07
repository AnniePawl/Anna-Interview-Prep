# Given list of ints, find first max element
# Print max element and its index 

def max_element(nums):
  max_num = max(nums)
  return max_num, nums.index(max_num)

print(max_element([1,2,3,2,1])) # 3 2 