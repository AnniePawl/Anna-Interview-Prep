# Given array of ints, rturn new array w/ each valuue doubled 

def double_array(nums):
  new_array = []
  for num in nums:
    new_array.append(num *2)
  return new_array


def double_array2(nums):
  return [num*2 for num in nums]

# Using Map 
def double_array_map(nums):
  return list(map(lambda s: s*2, nums))

print(double_array([1,2,3])) # [2,4,6]
print(double_array2([2,4,6])) # [4,8,12]
print(double_array_map([2,4,6])) # [4,8,12]




