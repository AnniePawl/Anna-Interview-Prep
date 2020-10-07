# Given a list of nums, return all nums w/ even indices 

def even_indices(nums):
  evens = []
  for i, num in enumerate(nums):
    if i% 2 == 0:
      evens.append(num)
  return " ".join(map(str,evens))

print(even_indices([5,6,7,8,9])) # 5 7 9

def even_indices2(nums):
  even_indices = [nums[i] for i in range(len(nums)) if i% 2 == 0]
  return " ".join(map(str,even_indices))

print(even_indices2([1,2,3,4,5,6])) # 1,3,5