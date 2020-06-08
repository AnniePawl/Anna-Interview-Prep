# Given array of ints in which each int appears 2x except 1, print single one. 

def lone_num(nums):
  for num in nums:
    if nums.count(num) == 1:
      return num

print(lone_num([2,2,1])) #1
print(lone_num([4,1,2,1,2])) #4