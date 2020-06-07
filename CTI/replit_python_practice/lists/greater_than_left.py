# Given list of numbers, find and print all elements greater than its next neighbor 


def greater_than_left(nums):
  list = []
  for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
      list.append(nums[i])
  return " ".join(map(str, list))

print(greater_than_left([1,5,2,4,3])) # [5,4]
print(greater_than_left([1,2,3, 4,5])) # [2, 3, 4, 5]

# CTI Solution 
for i in range(1, len(a)):
  if a[i - 1] < a[i]:
    print(a[i], end " ")