# Given a number n, count the number of primes between 2 and that number 
# Prime num --> only divisible by 1 and itself 

# Total time complexity is 0(n^2)
def count_primes(n):
  count = 0
  for i in range(2,n):  # O(n)
    if isPrime(i):
      count +=1 
  return count
  # Check every number in range 
    # Check if number is prime --> Helper function 
    #if number is prime 
      #increase count 

def isPrime(n): # O(n)
  # figure out if number is divisible by anything below it 
  for i in range(2,n):
    if n % i == 0:
      return False 
  return True 

print(isPrime(5)) # True
print(isPrime(4)) # False  
print(count_primes(10)) # 4
print(count_primes(15)) # 6

