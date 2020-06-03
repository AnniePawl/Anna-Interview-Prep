# Print decimal value of last two bits in reverse order

def dec_from_last_bits(num):
  binary = []
  while num > 0:
    if num % 2 == 0:
      binary.append(0)
      num = num //2 
    else:
      binary.append(1)
      num = num //2 
  reversed_2_bits = (binary[-2:])
  return reversed_2_bits
  # back to decmial 
  dec = 0 




print(dec_from_last_bits(3)) # 3
print(dec_from_last_bits(2)) # 1
print(dec_from_last_bits(37)) # 2