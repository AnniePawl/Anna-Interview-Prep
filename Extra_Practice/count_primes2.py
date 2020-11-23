# Given a number n, count the number of primes between 2 and that number 
# Prime --> num only divisible by 1 and itself, 

# Brute Force 
# Helper Function --> returns boolean
def isPrime(n):
  for i in range(2,n):
    if n % i == 0:
      return False
  return True

print(isPrime(3)) # True
print(isPrime(10)) # False
print(isPrime(11)) # True 

# Main Function --> int 

def countPrimes(n):
  count = 0
  for i in range(2,n):
    if isPrime(i):
      count +=1
  return count

print(countPrimes(10)) # 4
print(countPrimes(20)) # 8

