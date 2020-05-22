# Give a divisor and a bound, find largest n such that N divisiable by divisor, N less than or equal to bound, and N is greater than 0 

def max_multiple(divisor, bound):
  max_multiple = 0
  # for number in range 1 to bound:
  for num in range(1,bound+1):
    # check if divisor goes into num
    if num % divisor == 0:
      max_multiple = num
  return max_multiple

def max_multiple2(divisor, bound):
  return max(num for num in range(1,bound+1) if num % divisor == 0)

  


print(max_multiple(2,7)) # 6
print(max_multiple2(3,10)) # 9