# Given a number, return how many primes are in range from 2 to number(non-inclusive). 1 does not count as prime 


# Brute Force 
# Time Complexity: 0(n^2) = because nested for loop

# Helper Function 
def is_prime(n):
  for curr_num in range(2,n):
    if n % curr_num == 0:
      return False 
  return True
  
def count_primes_brute_force(n):
  count = 0 
  for num in range(2,n):
    if is_prime(num):
      count+=1
  return count


# print(is_prime(5)) # True
# print(is_prime(4)) # False
# print(is_prime(11)) # True

# print(count_primes_brute_force(10)) # 4
# print(count_primes_brute_force(20)) # 8


# Solution w/o Helper function 
# Strategy = Assume all true 


def count_primes(num):
  count = 0 
  primes = [True] * num # True for i in range(num) 
  for i in range(2,num):
    if primes[i] == True:
      count +=1 
      for j in range(i*i, num, i):
        primes[j] = False

  return count

# print("Count Primes V2 w/o heler function")
# print(count_primes(10)) # 4 
# print(count_primes(20)) # 8  



# Sieve of ERATOSTHENES 
# Most efficient solution O(nlognlogn)
# Even tho there are nested for loops, you are elimintaing numbers along the way so you're not actually checking/ testing every single number
# Strategy: Assume all true - then start removing mulitples and count remaining numbers 
def s_o_e(num):
  count = 0 
  primes = [True for i in range(num)]
  for i in range(2,num):
    if primes[i] is True:
      count +=1
      print(range(i*i, num, i))
      for j in range(i*i, num, i):
        primes[j] = False 
  return count

print("SOE Method")
print(s_o_e(10)) # 4 
# print(s_o_e(20)) # 8 

count_primes(12) # 5 
 
#  count = 2

#  2 3 4 5 6 7 8 9 10 11
#  T T F T F T F T  F   T 



