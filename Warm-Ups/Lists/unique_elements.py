# Given a list of nums, find and print the elements that only appear once. Print elements in order they appear in original list 

def unique_elements(nums):
  return [num for num in nums if nums.count(num) ==1]


print(unique_elements([4,3,5,2,5,1,3,5])) # 4,2,1


# Using Set - does not return output in correct order... 
def unique_elements2(nums):
  unique_elements = []
  for num in set(nums):
    if nums.count(num) == 1:
      unique_elements.append(num)
  return unique_elements
