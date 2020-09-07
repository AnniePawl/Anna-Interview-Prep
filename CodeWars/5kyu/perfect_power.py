# Perfect Power is positive int expressed as int power of anotehr positive intn
# Check whether given innt is perfect power. If so, return pair m and k with m^k = n. Otherwise return None of NULL. 
# Example --> 81 = 3^4 and 9^2, so (3,4) and (9,2) are valid solutions 

def isPP(n):
  # for numbers between 1 and half of n:
  position = 0
  for i in range(1,n//2+1):
    if i **
    # multiply num by every other num 
    # if product = n, return the pair 

print(isPP(4)) # [2,2]
print(isPP(9)) # [3,2]
print(isPP(5)) # None