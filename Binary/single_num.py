# Given an array of ints, every number appears twice, except for one. Find that one 

# Should be in linear runtime 

def single_num(nums):
  single_num = 0 
  for i in nums:
    single_num ^= i
  return single_num

print(single_num([2,2,1])) # 1
print(single_num([4,1,2,1,2])) # 4