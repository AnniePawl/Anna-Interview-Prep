# Given non-neg number, return last digit of factorial of N. 
def factorial(n):
  factorial = 1 
  for i in range(1, n+1):
    factorial = factorial * i 

  return str(factorial)[-1]


print(factorial(4))