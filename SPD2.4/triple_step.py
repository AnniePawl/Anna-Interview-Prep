# Triple Step: A child is running up a staircase with n steps. They can hop either 1 step, 2 steps, or 3 steps at a time. 
# Implement a method to count how many possible ways the child can run up the stairs 

# Example 
# Input: 4
# Examples outputs  [1,1,1,1], [1,1,2], [1,2,1], [2,2], [1,3]

def tripleStep(n):
  # Base cases 
  if (n < 0):
    return 0 
  elif (n == 0 or n == 1):
    return 1 
  # Use recursion to handle the rest 
  return tripleStep(n-1) + tripleStep(n-2) + tripleStep(n-3)

print(tripleStep(4))
print(tripleStep(2))
print(tripleStep(3))

