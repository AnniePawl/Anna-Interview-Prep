# Given two sorted arrays (a and b) of numbers and a target value, find a numberightfrom each array whose sum is closest to target.

a = [9, 13, 1, 8, 12, 4, 0, 5]
b = [3, 17, 4, 14, 6]
target = 20

# SOLUTION ONE 

def complex_two_sum(a, b, target):
  possible_solutions = []
  # make left and right pointers
  left= 0
  right= len(b) - 1
  # sort arrays   
  a = sorted(a) 
  b = sorted(b) 

  difference = abs(target - (a[left] + b[right]))
  while (left<= len(a) - 1) and (right>= 0): # O(nm)
      if abs(target - (a[left] + b[right])) < difference:
          
          possible_solutions = [(a[left], b[right])]
          difference = abs(target - (a[left] + b[right]))
      elif abs(target - (a[left] + b[right])) == difference:
          possible_solutions.append((a[left], b[right]))
      if (a[left] + b[right]) < target:
          left+= 1
      elif (a[left] + b[right]) > target:
          right-= 1
      elif (a[left] + b[right]) == target:
          left, right= left+1, right-1
  return possible_solutions

print(complex_two_sum(a,b,target))