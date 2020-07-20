# Given a number, return how many primes are in range from 2 to number(non-inclusive). 1 does not count as prime 

# Brute Force 
# O(n^2) double for loop
# Helper Function 
def is_prime(num):
  for current_number in range(2,num): 
    if num % current_number == 0 :
      return False 
  return True

def count_primes(num):
  count = 0 
  for number in range(2,num):
    if is_prime(number):
      count += 1 
  return count

print(is_prime(5)) # True
print(is_prime(4)) # False 
print(is_prime(2)) # True 
print(is_prime(9)) # False

print(count_primes(10)) # 4 
print(count_primes(20)) # 8

# Solution w/o helper function 
def count_primes2(num):
  count = 0 
  primes = [True] * num # [True for i in range(num)]
  for i in range(2,num):
    if primes[i] == True:
      count +=1
      for j in range(i*i, num, i ):
        primes[j] = False

  return count

print(count_primes2(10)) # 4
print(count_primes2(20)) # 8

# Sieve of Eratosthenes 
# Assume all are true - start removing multiples of something and count remanining numbers 
# O(nloglogn)
def s_o_e(n):
  # Start w/ assumption that everything is Prime
  count = 0 
  primes = [True for i in range(n)]
  for i in range(2,n):
    if primes[i] == True:
      count +=1
      for j in range(i*i, n, i):
        primes[j] = False 
  return count 

print("SOE method")
print(s_o_e(5))# 2
print(s_o_e(10)) # 4
print(s_o_e(20)) # 8

def range_practice(n):
  primes = [*range(n)]
  print(primes)
  for i in range(2,n):
    print(primes[i])

print("range practice")
print(range_practice(5))