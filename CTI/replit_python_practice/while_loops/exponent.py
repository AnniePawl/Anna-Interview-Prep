# Given x, find greatest integer n where 2**n is less than or equal to x. Return exponent value and result of expression 2^n 

def exponent(x):
  n = 0
  while 2 ** n <= x:
    n +=1 
  
  return n-1, 2**(n-1)


print(exponent(50)) # 5 32