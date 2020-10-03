# Given three nums, two of which are the same, return the position of the outlier 

def outlier(nums):
  for num in nums:
    if nums.count(num) == 1:
      return nums.index(num) +1


print(outlier([10,5,10])) # 2 
print(outlier([1,1,6])) # 3 
print(outlier([8,12,12])) # 1