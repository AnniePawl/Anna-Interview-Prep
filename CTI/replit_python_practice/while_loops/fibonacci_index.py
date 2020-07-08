# Given a positive integer, determine if it's the nth fibonacci numer for some n. If so, print n, else print -1 

# Fibonacci code 
def fib_index(n):
  fib_list = [0,1]
  while n >=2:
    fib_list.append(fib_list[-1] + fib_list[-2])
    n -= 1 
  

 
print(fib_index(4)) # -1
print(fib_index(8)) # 6 
print(fib_index(34)) # 9 