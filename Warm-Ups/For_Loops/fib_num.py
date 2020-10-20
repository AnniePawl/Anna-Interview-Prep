# Given a num n, return nth fib number


def fib_number(n):
  prev, next = 1,1
  for i in range(n-2):
    prev, next = next, prev+next
  return next


print(fib_number(3)) # 2
print(fib_number(6)) # 8
print(fib_number(8)) # 21