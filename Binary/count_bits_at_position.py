# Given 5 input numbers (a,b,c,d,n), print number of 1 bits at nth least significant bit position for a,b,c,d

def count_bits(a,b,c,d,n):
  count = 0 
  num = 6 
  print(bin(6>>n))

print(count_bits(1,1,1,1,0)) # 4
# Explaination: All numbers a, b, c and d are 1 - binary equivalent of which is 0001. Since n is 0 in the input, nth lsb position is the last bit position. In all four numbers, the last bit position is 1, counting them results in 4.
print(count_bits(2,3,5,6,1)) # 3


