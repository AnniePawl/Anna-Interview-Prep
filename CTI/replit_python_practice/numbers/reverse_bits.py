# Given an integer greater than 9, print the number created by reversing the bits. Combine the reversed bits to create the decimal value represented by the reversed bits and print the decimal value.

def reverse_bits(num):
  reversed_bit = bin(num)[::-1]
  num = int(str(reversed_bit[:-2]), 2)
  return num

print(reverse_bits(37)) # 41

