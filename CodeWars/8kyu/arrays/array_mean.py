# Find Average of list of numbers in array 

def average(nums):
  return sum(nums) /len(nums) if nums else 0

#  "if nums" checks is list is empty --> same as writing "if len(nums) > 0"

print(average([1,2,3,4,5,6])) # 3
print(average([1,3,5,7])) # 4
print(average([])) # 0