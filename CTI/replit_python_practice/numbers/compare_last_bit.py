# Given two input numbers, print "True" if last least significant bit of two numbers match, "False" if not. 


# Inputs 
# a = int(input())
# b = int(input())


def compare_last_bits(a,b):
  if bin(a)[-1] == bin(b)[-1]:
    return True 
  return False

print(compare_last_bits(3,5)) # True  
print(compare_last_bits(5,8)) # False
print(compare_last_bits(6,8)) # True  