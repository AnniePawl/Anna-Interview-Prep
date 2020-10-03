# Returns largest sum of contiguous subarray

def maxSubArray(nums):
  max = nums[0]
  for i in range(len(nums)-1):
    if nums[i] + nums[i+1] > max>



 

print(maxSubArray(3)) # 3
print(maxSubArray([-2,-1,-3,4,-1,2,1,-5,4])) 
# 6 b/c [4,-1,2,1] returns 6