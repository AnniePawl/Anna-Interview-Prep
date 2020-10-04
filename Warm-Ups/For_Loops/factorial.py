# Return n factorial 

def factorial(n):
  if n == 1:
    return 1 
  else:
    return n * factorial(n-1)

print(factorial(3)) # 6
print(factorial(4)) # 24