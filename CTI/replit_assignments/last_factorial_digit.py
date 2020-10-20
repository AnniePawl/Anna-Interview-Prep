# Given non-neg number, return last digit of factorial of N. 

# Factorial Brute Force
def factorial(n):
  factorial = 1
  for num in range(1, n+1):
    factorial = factorial * num
  return factorial

# Factorial Recursive
def factorial_recursive(n):
  if n == 0:
    return 1 
  return n * factorial_recursive(n-1)


# Return Last Digit of Factorial 
def last_factorial(n):
  if n == 0:
    return 1 
  factorial =  n * factorial_recursive(n-1)
  return [int(x) for x in str(factorial)][-1]


print(factorial(3)) # 6
print(factorial(6)) # 0 (b/c 720)

print(factorial_recursive(3)) # 6
print(factorial_recursive(6)) # 0 (b/c 72)

print(last_factorial(3)) # 6
print(last_factorial(6)) # 0 (b/c 720)
print(last_factorial(4)) # 4 (b/c 24)


