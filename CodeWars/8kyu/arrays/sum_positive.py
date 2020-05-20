# Given an array of numbers, return sum of positive nums 

def sum_positive(nums):
  sum = 0 
  for num in nums:
    if num > 0:
      sum += num 
  return sum

def sum_positive2(nums):
  return sum(num for num in nums if num > 0)


print(sum_positive([-1,-2,1,2])) # 3 

print(sum_positive2([-1,-2,1,2])) # 3 