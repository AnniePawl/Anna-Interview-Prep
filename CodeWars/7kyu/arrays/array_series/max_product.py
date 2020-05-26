# Given an array of ints, Find product of k max numbers 

def maxProduct(nums, n):
  nums = sorted(nums)
  product = 1
  for num in nums[-(n):]:
    product = product * num
  return product


print(maxProduct([4,3,5], 2)) # 20
print(maxProduct([4,3,5,10,8,2], 3)) # 400
