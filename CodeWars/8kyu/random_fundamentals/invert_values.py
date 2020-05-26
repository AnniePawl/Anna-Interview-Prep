def invert(nums):
  return [num*-1 for num in nums]

def invert2(nums):
  return [-x for x in nums]

print(invert([1,2,3])) # [-1,-2,-3]
print(invert([])) # []
print(invert([-1,5,-10])) # [1,-5,10]