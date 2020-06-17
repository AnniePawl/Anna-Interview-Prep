# Return True if first and last num in string are same 

def same_first_last(nums):
  return nums[0] == nums[-1]

print(same_first_last([10,20,30,40])) # False 
print(same_first_last([10,20,30,10])) # True
