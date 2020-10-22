# Given arr of ints as stings and nums, return sum of array of values as if all were numbers 


def sum_mix(nums):
  return sum(map(int, nums))

print(sum_mix([1,"2",3,"4"])) # 10