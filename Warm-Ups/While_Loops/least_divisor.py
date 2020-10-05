# Given an int greater than 2, print it's smallest int divisor greater than one 


def least_divisor(num):
  divisor = 2
  while num % divisor != 0:
    divisor +=1
  if num % divisor == 0:
    return divisor 
  

print(least_divisor(15)) # 3 
print(least_divisor(7)) # 7
print(least_divisor(4)) # 2