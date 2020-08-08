# Given 5 input numbers (a,b,c,d,n), print number of 1 bits at nth least significant bit position in all four numbers (a,b,c,d)

def count_bits_at_position(a,b,c,d,n):
  pass 

print(count_bits_at_position('11110')) # 4
# All numbers a, b, c and d are 1 - binary equivalent of which is 0001. Since n is 0 in the input, nth lsb position is the last bit position. In all four numbers, the last bit position is 1, counting them results in 4.

print(count_bits_at_position('23561')) # 3