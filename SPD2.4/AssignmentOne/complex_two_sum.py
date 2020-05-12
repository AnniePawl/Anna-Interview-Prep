# Given two sorted arrays (a and b) of numbers and a target value, find a number from each array whose sum is closest to target.

a = [9, 13, 1, 8, 12, 4, 0, 5]
b = [3, 17, 4, 14, 6]
target = 20

# SOLUTION ONE 
# Time Complexity: 
# Space Complexity: 
def complex_two_sum_v1(a, b, target):
  a.sort()
  b.sort()

  results = []
  left = 0 
  right = len(b)-1

  # find differences
  while(left < len(b))

  

 

print("Testing complex two sum v1: ")
print(complex_two_sum_v1(a, b, target))
# [13,6], [4,17], or [5,14]

# SOLUTION TWO 
# Time Complexity: O
# Space Complexity: 