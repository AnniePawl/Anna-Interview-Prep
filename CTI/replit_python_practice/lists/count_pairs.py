# Given list of nums, count number of pairs of equal elements. Any two elements that are equal should count as a pair 

def count_pairs(nums):
  pairs = 0 
  for i in range(len(nums)):
    if nums[i] == nums[i+1]

print(count_pairs([1,1,1])) # 3
print(count_pairs([1,1,1,1])) # 6
print(count_pairs([1,2,3,2,3])) # 2
print(count_pairs([1,1,1,1,1])) # 10