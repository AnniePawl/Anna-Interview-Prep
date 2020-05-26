#  Element if "leader" if greater than sum of all elements to it's right side 

def leaders(nums):
  leaders = []
  for i in range(len(nums)):
    if nums[i] > sum(nums[i+1:]):
      leaders.append(nums[i])
  return leaders

def leaders2(numbers):
  return [n for (i,n) in enumerate(numbers) if n > sum(numbers[(i+1):])]

print(leaders([1,2,3,4,0])) # [4]
print(leaders([16,17,4,3,5,2])) # [17,5,2]
print(leaders([-1,-26,-2])) # [-1]

print(leaders2([1,2,3,4,0])) # [4]
print(leaders2([16,17,4,3,5,2])) # [17,5,2]
print(leaders2([-1,-26,-2])) # [-1]