# Given list of positive ints, print row with len(ints) + 1 entries 
# Fist and last num should be 1 
# ith num should be sum of values of ith-1 and ith num in list of ints 

def pascals2(nums):
  new_nums = [nums[0]]
  for i in range(len(nums)-1):
    new_nums.append(nums[i]+ nums[i+1])
  new_nums.append(nums[-1])
  return new_nums
 

print(pascals2([1,3,3,1])) # 1 4 6 4 1
print(pascals2([1,5,10,5,1])) # 1,6,15,15,6,1 