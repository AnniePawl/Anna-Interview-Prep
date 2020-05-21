# Given integer arrays a,b - create program that returns true is sum of squared elements in a is greater than sumr of cubes in b 


def array_madness(a,b):
  squared_a = [num**2 for num in a]
  cubed_b = [num**3 for num in b]
  sum_a = sum(num for num in squared_a)
  sum_b = sum(num for num in cubed_b)
  if sum_a > sum_b:
    return True 
  return False

def array_madness2(a,b):
  return sum(num**2 for num in a) > sum(num**3 for num in b)
  


print(array_madness([4,5,6], [1,2,3])) # True 
print(array_madness([1,2,3], [3,4,5])) # False 


print(array_madness2([4,5,6], [1,2,3])) # True 
print(array_madness2([1,2,3], [3,4,5])) # False 
