# Return factorial of input num 
def factorial(n):
  if n == 1:
    return n 
  else:
    return n * factorial(n-1)


def factorial_sum(n):
  sum = 0 
  while n > 0:
    sum += factorial(n)
    n = n -1
  return sum


print(factorial(4)) # 24
print(factorial_sum(4)) # 33

