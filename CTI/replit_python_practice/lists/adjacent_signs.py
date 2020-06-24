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


a = [int(x) for x in input().split()]
pair = False
for i in range(len(a)-1):
  if (a[i] > 0 and a[i+1] >0):
    print(a[i], a[i+1])
    pair = True
    break
  elif (a[i] < 0 and a[i+1] <0):
    print(a[i], a[i+1])
    pair = True
    break
if pair == False:
  print(0)


# CTI Solution 
# Trick - use multiplication - both pos* pos and neg* neg = pos
a = [int(s) for s in input().split()]
for i in range(1, len(a)):
  if a[i - 1] * a[i] > 0:
    print(a[i - 1], a[i])
    break
else:
  print(0)