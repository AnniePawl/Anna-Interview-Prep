# Given a number, print its last two bits 

def last_two_bits_brute_force(num):
  binary = []
  while num > 0 :
    if num % 2 == 0:
      binary.append(0)
      num = num //2
    else:
      binary.append(1)
      num = num //2 
  return "".join(map(str,binary[::-1][-2:]))


print(last_two_bits_brute_force(1234)) # 10
print(last_two_bits_brute_force(548)) # 00
print(last_two_bits_brute_force(999)) # 11


# Using bitwise operators .... 
def last_two_bitwise(num):


print("Last Two using bitwise operator")
print(last_two_bitwise(1234)) # 10
print(last_two_bitwise(548)) # 00
print(last_two_bitwise(999)) # 11
