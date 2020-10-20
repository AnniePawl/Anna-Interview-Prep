# Given an int, return the decimal value of last two bits in reverse order

# Not super efficient. Whoops
def swaped_bits_value(num):
  bits = []
  while num > 0:
    if num % 2 == 0:
      bits.append(0)
      num = num //2 
    else:
      bits.append(1)
      num = num // 2
  
  reversed_last_two = "".join(map(str,bits[-2:][::-1]))
  return int(reversed_last_two,2)
  
  
  
 

  
  
print(swaped_bits_value(3)) # 3 
print(swaped_bits_value(37)) # 2



