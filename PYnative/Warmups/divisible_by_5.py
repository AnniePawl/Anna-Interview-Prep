# Given list of nums, return those divisible by 5 

def divisible_by_5(nums):
  div_by_5 = []
  for num in nums:
    if num % 5 == 0:
      div_by_5.append(num)
  return div_by_5

print(divisible_by_5([10,20,33,45,53])) # 10,20,45