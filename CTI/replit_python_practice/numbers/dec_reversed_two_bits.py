# Given int > 9, return decimal value of last 2 bits in reverse order. 
def dec_of_last_bits(num):
  binary = []
  while num > 0:
    if num % 2 == 0: 
      binary.append(0)
      num = num // 2
    else:
      binary.append(1)
      num = num //2
 
  last_two = binary[::-1][-2:]
  last_two_reversed = last_two[::-1]
 
  # now revert back to decimal 
  decimal = 0
  bits = last_two_reversed[::-1]
  for i in range(len(bits)):
    if bits[i] ==1 :
      decimal += 2 ** i
  return decimal

# CTI solution ? No working on 37 ... 
def dec_of_last_bits2(num):
  return num % 100

print("Decimal of last two bits in reverse order")
print(dec_of_last_bits(37)) # 2 
print(dec_of_last_bits(3)) # 3

print(dec_of_last_bits2(37)) # 2 
print(dec_of_last_bits2(3)) # 3


