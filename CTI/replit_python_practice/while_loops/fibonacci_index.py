# Given a positive integer, determine if it's the nth fibonacci numer for some n. If so, print n, else print -1 

# Find index of given fib number 
# Doesn't handle case if number isn't fib 
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

print(fib_index(8)) # 6 
print(fib_index(34)) # 9 
print(fib_index(3)) # 4
print(fib_index(1134903170)) # 45

def fib_index2(n):
  



print("Fib 2")
print(fib_index2(8)) # 6 
print(fib_index2(34)) # 9 
print(fib_index2(3)) # 4
print(fib_index2(1134903170)) # 45
# print(fib_index2(4)) # -1 b/c doesnt exist








# This code takes TOO LONG for big inputs
    # fib_list = [1,1,2]
    # for num in range(n-2):
    #   fib_list.append(fib_list[-1]+fib_list[-2])

    # if n in fib_list:
    #   return fib_list.index(n) + 1
    # else:
    #   return -1

  




