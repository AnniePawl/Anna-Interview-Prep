# Given a 2 bit integer, print its left bit (a 2's bit) and then its right bit (a ones bit). Use the operator of integer division for obtaining the 2's bit and the operator of taking remainder for obtaining the ones bit.

def two_bits(num):
  binary = []
  while num > 0:
    if num % 2 == 0:
      binary.append(0)
      num = num //2
    else: 
      binary.append(1)
      num = num //2
 
  return "".join(map(str, binary[::-1]))


# Print last 2 bits of an integer greater than 9, with space in between 

def last_two(num):
  binary = []
  while num > 0:
    if num % 2 == 0:
      binary.append(0)
      num = num //2
    else: 
      binary.append(1)
      num = num //2
 
  return " ".join(map(str, (binary[::-1])[-2:]))


# Return bits in reverse order w/ space in between
def reverse_bits(num):
  binary = []
  while num > 0 :
    if num % 2 == 0:
      binary.append(0)
      num = num //2 
    else:
      binary.append(1)
      num = num //2 
  return " ".join(map(str, binary)) # already reversed .. 



  


print("Reverse Bits w/ Space ")
print(reverse_bits(37)) # 1 0 1 0 0 1

print("Two Bits")
print(two_bits(2)) # 1 0
print(two_bits(3)) # 1 1
print(two_bits(1)) # 0 1
print(two_bits(10)) # 1 0 1 0
print(two_bits(37)) # 1 0 1 0


print(last_two(37)) # 0 1


