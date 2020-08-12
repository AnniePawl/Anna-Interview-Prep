# Given two input numbers, print new numbers whose binary value is shifted right by 1 bit 

# >>  bitwise operator shifts bits over specified amount 
# int(blank, 2) will convery binary string back to int

def remove_last_bit(a, b):
  shifted_a = bin(a>>1)
  shifted_b = bin(b>>1)
  return int(shifted_a,2), int(shifted_b,2)

print(remove_last_bit(3,5)) # 1,2
print(remove_last_bit(6,8)) # 3,4
print(remove_last_bit(5,8)) # 2,4