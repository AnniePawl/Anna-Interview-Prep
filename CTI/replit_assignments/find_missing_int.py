# Given unsorted int array, find first missing positive integer 
# Algorithm should run in O(n)time

def find_pos(nums):
  sorted_nums = nums.sort()
  for i, j in enumerate(sorted_nums):
    if nums[i] > 0:
      if nums[i+1] - nums[i] != 1:
        return nums[i+1]
  return 1

  
      


print(find_pos([1,2,0])) # 3
print(find_pos([3,4,-1,1])) # 2
print(find_pos([-8,-7,-6])) # 1