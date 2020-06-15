# Given int, return count of "1" bits the number has when converted as 32 bit unsinged int

def count_set_bits(num):
  binary = []
  while num > 0:
    if num % 2 == 0:
      binary.append(0)
      num = num //2 
    else:
      binary.append(1)
      num = num //2
  return binary.count(1)

  
print(count_set_bits(1)) # 1 
print(count_set_bits(2)) # 1 
print(count_set_bits(3)) # 2 
print(count_set_bits(5)) # 2
print(count_set_bits(500)) # 6


# CTI SOLUTION

def count_set_bits2(num):
  count = 0
  while num > 0:
      num &= num - 1
      count += 1
  return count


print(count_set_bits2(1)) # 1 
print(count_set_bits2(2)) # 1 
print(count_set_bits2(3)) # 2 
print(count_set_bits2(5)) # 2
print(count_set_bits2(500)) # 6
