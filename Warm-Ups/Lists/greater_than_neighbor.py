# Given a list of nums, find and print all elements that are greater than left neighbor 


def greater_than_left(nums):
  result = []
  for i in range(len(nums)-1):
    if nums[i] < nums[i+1]:
      result.append(nums[i+1])
  return result

print(greater_than_left([1,5,2,4,3])) #5,4