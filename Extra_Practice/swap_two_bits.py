# Given 2 bit int, print last two bits in reverse order. 

def swap_two_bits(num):
  return str(num%2) + " " + str(num//2)

print(swap_two_bits(2)) # 0 1 
print(swap_two_bits(3)) # 1 1 

def swap_two_bits2(num):
  bits = []
  while num > 0:
    if num % 2 == 0:
      bits.append(0)
      num = num // 2 
    else:
      bits.append(1)
      num = num //2
  return " ".join(map(str,bits))

print(swap_two_bits2(2)) # 0 1 
