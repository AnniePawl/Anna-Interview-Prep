# Given a list of numbers, count how many are zero 

def count_zeros(nums):
  count = 0 
  for num in nums:
    if num == 0:
      count += 1
  return count

print(count_zeros([60,4,0,34,0,45,0])) # 3

def count_zeros2(nums):
  return sum(1 for num in nums if num ==0)

print(count_zeros2([60,4,0,34,0,45,0])) # 3