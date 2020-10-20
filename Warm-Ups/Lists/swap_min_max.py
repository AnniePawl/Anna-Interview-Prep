# Given list of distinct nums, swap min and max, print resulting list


def swap_min_max(nums):
  min_i = nums.index(min(nums))
  max_i = nums.index(max(nums))

  nums[min_i], nums[max_i] = nums[max_i], nums[min_i]

  return nums


print(swap_min_max([3,4,5,2,1])) # [3,4,1,2,5]