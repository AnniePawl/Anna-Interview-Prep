# Return the nth fibonacci number 

def fibonacci(n):
  # base cases
  if n == 0:
    return 0 
  if n == 1:
    return 1 
  if n > 1:
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))

# This can handle Huge input b/c of memoization
fib_cache = {}
def fib_num(n):
  if n in fib_cache:
    return fib_cache[n]
  # compute nth num 
  if n == 1:
    value = 1
  if n == 2:
    value = 1
  if n > 2:
    value = fib_index2(n-1) + fib_index2(n-2)
  
  fib_cache[n] = value
  return value

# Return list of first n fibonacci numbers
def fibonacci_list(n):
  if n == 0:
    return [0]
  if n == 1:
    return [0,1]
  else:
    fib_list = fibonacci_list(n-1)
    fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

print(fibonacci_list(6)) # [1,1,2,3,5,8]

# CTI Soltition 
# prev, next = 1, 1
# n = int(input())
# for i in range(n-2):
#   prev, next = next, prev + next
# print(next )