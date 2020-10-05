# Fibonacci numbers are the numbers in the integer sequence starting with 1, 1 where every number after the first two is the sum of the two preceding ones:

# DOESNT WORK

# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# Given a positive integer, determine if it's the nth Fibonacci number for some n. If it is, print such n, otherwise print -1.

def fib_index(n):
  if n <= 1:
    return n
  
  a = 0 
  b = 1 
  c = 1 
  res = 1 
  while c < n :
    c = a + b 
    res +=1
    a = b 
    b = c
  return res  

print(fib_index(8)) # 6 (6th fib number)
print(fib_index(7)) # -1 (not a fib number)