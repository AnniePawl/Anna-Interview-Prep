# Given a list of integers, find max difference between successive elements in sorted form 

def max_gap(nums):
  nums = sorted(nums)
  gap = 0
  for i in range(len(nums)-1):
    diff = abs(nums[i] - nums[i+1])
    if diff > gap:
      gap = diff 
  return gap
 
def max_gap2(nums):
    A = sorted(nums)
    return max([abs(A[i] - A[i+1]) for i in range(len(A)-1)])

def max_gap3(nums):
    lst = sorted(nums)
    return max(b-a for a,b in zip(lst, lst[1:]))


print(max_gap([13,10,5,2,9])) # 4
# when sorted, max gap = 4 b/c 9-5 = 4

print(max_gap2([13,10,5,2,9])) # 4
print(max_gap3([13,10,5,2,9])) # 4

