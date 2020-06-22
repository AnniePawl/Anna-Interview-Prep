# Given a positive integer, determine if it's the nth fibonacci numer for some n. If so, print n, else print -1 

# Fibonacci code 

prev, next = 1, 1
n = int(input())
for i in range(n-2):
  prev, next = next, prev + next
print(next)


def fib_index(n):
  fib_nums = []
  prev, next =  1, 1
  for i in range(n-2):
    prev,next = next, prev + next
  fib_nums.append(next)
  return fib_nums



print(fib_index(8)) # 6 
print(fib_index(34)) # 9 