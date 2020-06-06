# Given integer > 2, print it's smallest int divisor > 1 

def smallest_divisor(num):
  divisor = 2
  while num % divisor != 0:
    divisor +=1 
  return divisor
  # if num % divisor == 0 :
  #   return divisor
 

print(smallest_divisor(15)) # 3
print(smallest_divisor(20)) # 2