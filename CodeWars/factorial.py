# Calculate factorial for given input  

# Using recursion
def factorial(n):
  # base case 
  if n == 0 or n == 1:
    return n 
  else: 
    return n* factorial(n-1)

print(factorial(3)) # 6
print(factorial(5)) # 120 
print(factorial(7)) # 5040 