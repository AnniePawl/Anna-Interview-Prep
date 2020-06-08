# Given list of ints, find first pair of adjacent elements w/ same sign. If no pair, print 0 

def adjacent_pairs(nums):
  for i in range(len(nums)-1):
    if nums[i] > 0 and nums[i+1] > 0:
      return " ".join(map(str,[nums[i+1], nums[i]]))
    elif nums[i]  < 0 and nums[i+1] < 0:
      return " ".join(map(str,[nums[i+1], nums[i]]))
  return 0
  
   

print(adjacent_pairs([-1,2,3,-1,-2])) # 2 3 
print(adjacent_pairs([1, -2,-3, 1,-2])) # -2 -3 
print(adjacent_pairs([1,-3,4,-3])) # 0

