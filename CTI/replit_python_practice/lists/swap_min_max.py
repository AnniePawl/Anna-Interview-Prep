# Swap min and max in list of nums 

def swap(nums):
  max_index = nums.index(max(nums))
  min_index = nums.index(min(nums))
  min_num = min(nums)
  max_num = max(nums)

  nums[max_index] = min_num
  nums[min_index] = max_num

  return nums


print(swap([3,4,5,2,1])) # 3,4,1,2,5