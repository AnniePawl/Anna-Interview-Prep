# Given an int, return its last two bits 

# Method One (using bitiwse operators) ??


# Method Two (long form)
def last_two_bits(num):
  bits = []
  while num > 0:
    if num % 2 == 0:
      bits.append(0)
      num = num // 2
    else:
      bits.append(1)
      num = num // 2
  return bits[::-1][-2:]
  

# print(last_two_bits(5)) # 0 1
# print(last_two_bits(37)) # 0 1
# print(last_two_bits(3)) # 1 1