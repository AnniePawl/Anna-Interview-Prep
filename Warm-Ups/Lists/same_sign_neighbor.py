# Given a list of nums, find and print first adjacent pair of elements that has same sign. If no such pair, print 0 

def same_sign(nums):
  for i in range(len(nums)-1):
    if nums[i] * nums[i+1] > 0:
      return nums[i], nums[i+1]
  else:
    return 0
      
      

print(same_sign([-1,2,3,-1,-2])) # [2,3]
print(same_sign([1,-3,4,-1])) # 0 