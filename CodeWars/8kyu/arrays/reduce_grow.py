# Given array of ints, return result of multiplying values togeher in order 

def mult_array(nums):
  result = 1 
  for num in nums:
    result = result* num 
  return result

# Using Lambda
def mult_array2(nums):
  return reduce(lambda x,y: x* y, nums)


print(mult_array([1,2,3])) # 6 
print(mult_array([2,2,2,2])) # 16 