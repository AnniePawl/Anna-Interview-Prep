# Given integer > 2, print it's smallest int divisor > 1 

def smallest_divisor(num):
  divisor = 1
  while num % divisor != 0:
    if num % divisor == 0 :
      return divisor
    else:
      divisor +=1 
    

print(smallest_divisor(15)) # 3
print(smallest_divisor(20)) # 2