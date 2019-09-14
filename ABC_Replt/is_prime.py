# Count the number of prime numbers less than a non-negative number, n

# Give 10, solution should return 4
# 1 does not count as prime
# Divide into 2 functions


# Determine if inut is prime
def isPrime(n):
    for current_number in range(2, n):
        if n % current_number == 0:
            return False
    return True

# print(isPrime(7))


# Determine how many prime numbers are UNDER this input number
def countPrime(n):
    count = 0
    for current_number in range(2, n):
        if isPrime(current_number) is True:
            count += 1
    return count


print(countPrime(20))
