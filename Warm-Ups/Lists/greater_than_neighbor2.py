# Given a list of numbers, determine and print number of elements that are greater than both their neighbors

def greater_than_neighbors2(nums):
  count = 0
  for i in range(1,len(nums)-1):
    if nums[i] > nums[i-1] and nums[i]> nums[i+1]:
      # result.append(nums[i])
      count +=1
  return count

print(greater_than_neighbors2([1,5,1,5,1])) # 2