# Given list of nums, print elements that only appear once. 

def appear_once(nums):
  once = []
  for num in nums:
    if nums.count(num) == 1:
      once.append(num)
  return once

def appear_once2(nums):
  return " ".join(map(str,[num for num in nums if nums.count(num)==1]))



print(appear_once([4,3,5,2,1,3,5])) # [4,2,1]
print(appear_once2([4,3,5,2,1,3,5])) # [4,2,1]

# CTI SOLUTION 
a = [int(s) for s in input().split()]
for i in a:
  if a.count(i) == 1:
    print(i, end=' ')
