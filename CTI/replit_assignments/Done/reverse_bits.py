# Given an integer n, reverse its first 32 bits, and return the reversed-bit integer.


def reverse_bits(n):
  result = 0
  for i in range(32):
      result <<= 1
      result |= n & 1
      n >>= 1
  return result
  

print(reverse_bits(5)) #2684354560


def reverse_bits2(num):
	rev = 0
	for i in range(32):
		if num & (1 << i):
			rev |= (1 << (32 - i - 1))
	return rev