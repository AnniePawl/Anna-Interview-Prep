# Given a 2 bit integer, print its left bit and right bit. Use operator of integer division to obrain 2's bit, and modulo to obtain 1's bit. 


def two_bits(num):
  return num // 2, num % 2

print(two_bits(2)) # 1 0 
print(two_bits(3)) # 1 1