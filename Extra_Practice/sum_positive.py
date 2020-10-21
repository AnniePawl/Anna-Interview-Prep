# Given an array of nums, return sum of all positive digits 


def sum_positive(arr):
  return sum(num for num in arr if num >0)

print(sum_positive([1,-3,4,-2])) # 5