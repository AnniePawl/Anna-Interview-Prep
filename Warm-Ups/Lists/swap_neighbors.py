# Given list of numbers, swap adjacent elements in each pair. Print new list. If odd num of elements, leave last element intact 

def swap_elements(nums):
  for i in range(0,len(nums)-1,2):
    nums[i], nums[i+1] = nums[i+1], nums[i]
  return nums
  

print(swap_elements([1,2,3,4,5]))
# [2,1,4,3,5]

print(swap_elements([9,8,7,6])) # 8,9,6,7