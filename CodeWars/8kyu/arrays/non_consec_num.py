# Find and return first non-consecutive number in array

def first_non_consec(nums):
  for i in range(len(nums)-1):
    if nums[i+1] != nums[i] + 1:
      return nums[i+1]
  

print(first_non_consec([1,2,3,4,6,7,8])) # 6
print(first_non_consec([10,11,13,45])) # 13
print(first_non_consec([20,21,22])) # None
print(first_non_consec([-4,-3,-1, 0])) # -1