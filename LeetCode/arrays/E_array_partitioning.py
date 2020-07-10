# Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

def partitioning(nums):
  nums.sort() # 0(nlogn)
  return sum(nums[::2])

print(partitioning([1,4,3,2])) # 4 
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).