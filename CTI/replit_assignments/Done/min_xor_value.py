# Given list of unsigned ints, find pair of ints in array that have min XOR value. Return that min XOR value
# Bitwise XOR sets the bits in the result to 1 if either, but not both, of the corresponding bits in the two operands is 1.
# XOR --> a ^ b

def min_xor(nums): 
  min = nums[0] ^ nums[1]
  for i in range(len(nums)-1):
    while i < len(nums)-1:
      if nums[i] ^ nums[i+1] < min:
        min = nums[i] ^nums[i+1]
      i +=1
  return min



print(min_xor([0,2,5,7])) # 2 (0 XOR 2)
print(min_xor([0,4,7,9])) # 3 (4 XOR 7)


def min_xor_value(integers):
  integers = sorted(integers)
  minimum_xor = integers[0] ^ integers[1]
  for index in range(1,len(integers)):
    if integers[index] ^ integers[index-1] < minimum_xor:
      minimum_xor = integers[index] ^ integers[index-1]
  return minimum_xor
  