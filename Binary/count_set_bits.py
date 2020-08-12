# Given an interger value, return count of "1" bits when converted to 32-bit unsigned integer 


def count_set_bits(num):
  count = 0
  while num > 0:
      num &= num - 1
      count += 1
  return count

  
print(count_set_bits(1)) # 1
print(count_set_bits(3)) # 2
print(count_set_bits(500)) # 6


# Kind of cheating.. 
# Runtime: Count = O(n), bin() = O(log(n)) --> O(n)
def count_set_bits2(num):
  return bin(num).count("1")