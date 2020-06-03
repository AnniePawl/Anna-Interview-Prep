#  Given an array or ints, return a series of numbers from 0 to highest number - but if array contains any duplicates, you must return [0]

def series(nums):
  biggest_num = max(nums)
  for num in nums:
      if nums.count(num) > 1:
          return [0]
          break
  
  return [x for x in range(biggest_num + 1)]


def complete_series(a):
  return list(range(max(a) +1)) if len(a) == len(set(a)) else [0]


print(series([2,1])) # [0,1,2]
print(series([2,1,4,0,6])) # [0,1,2,3,4,5,6]
print(series([2,1,4,0,6,4])) # [0]
print(series([0])) # [0]


print(complete_series([2,1])) # [0,1,2]
print(complete_series([2,1,4,0,6])) # [0,1,2,3,4,5,6]
print(complete_series([2,1,4,0,6,4])) # [0]
print(complete_series([0])) # [0]