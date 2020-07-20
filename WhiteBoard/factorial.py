# Given a number, return it's factorial 

# Recursive Approach 
def factorial(n):
  if n == 0: # base case
    return 1
  return  n * factorial(n-1)

print(factorial(3)) # 6
print(factorial(6)) # 720
print(factorial(9)) # 363880


# Print Last digit of factorial 
def last_factorial_digit(n):
  if n == 0:
    return 1 
  factorial = n*last_factorial_digit(n-1)
  return [int(x) for x in str(factorial)] [-1]


print(last_factorial_digit(6)) # 0
print(last_factorial_digit(9)) # 0

