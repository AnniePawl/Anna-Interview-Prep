# Count number of primes less than given number n. 1 does not count as prime

# PSEUDOCODE  CountPrime 
# Given input 
# For every num under input:
  # Check to see if num prime 
  # If it is:
    # Mark as prime 
  # If not:
    # Mark as not prime 
# Return count of  prime numbers 

# PSEUDOCODE IsPrime
# Given input:
# For every number under input:
  # Check if it's devisible by ...



# Determine if the input number is prime 
def isPrime(n):
  for current_number in range(2,n):
    # if the input number is evenly divisible by the current number?
    if n % current_number == 0:
      return False
  return True

# Determine how many prime numbers are UNDER the input number
def countPrimes(n):
  return sum(1 for num in range(2,n) if isPrime(num))


def countPrimes2(n):
  count = 0
  for num in range(2,n):
    if isPrime(num):
      count += 1
  return count



print(countPrimes(10)) # 4
print(countPrimes(20)) # 8

print(countPrimes2(10)) # 4
print(countPrimes2(20)) # 8


def isPrime(n):
    for current_number in range(2,n):
      if n % current_number == 0:
          return False
    return True    

def countPrimes(n):
    count_of_primes = 0
    for current_number in range(2,n):
      # check to see if the number is prime
      if isPrime(current_number):
          count_of_primes += 1
    return count_of_primes
countPrimes(40)
