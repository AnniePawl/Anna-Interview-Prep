# Given integer n, return number of trailing zeros in n 
# Time complexity should be logarithmic 
# Trailing zeros start at 5!, double at 10!, triple at 15!, quad at 20! 

def trailing_zeros_factorial(n):
  trailing_zeros = 0 
  i = 5 # powers of 5 
  while n // i >= 1:
    trailing_zeros += n // i 
    i *= 5 
  return trailing_zeros


print("The number of trailing zeros is:" + str(trailing_zeros_factorial(5))) # 1
print("The number of trailing zeros is:" + str(trailing_zeros_factorial(10))) # 2
print("The number of trailing zeros is:" + str(trailing_zeros_factorial(15))) # 3
print("The number of trailing zeros is:" + str(trailing_zeros_factorial(20))) # 4