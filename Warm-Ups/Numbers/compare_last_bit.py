# Given two numbers, return TRUE is least significant bits are the same. Otherwise, return FALSE

def compare_last_bit(a,b):
  return bin(a)[-1] == bin(b)[-1]

print(compare_last_bit(3,5)) # True 
print(compare_last_bit(3,10)) # False
print(compare_last_bit(6,8,)) # True
