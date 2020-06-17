# Given list of nums, return number of elements that are greater than both their neighbors 


# input = [int(x) for x in input().split()] 
# print(input)


def greater_than_neigbors(nums):
  result = []
  for i in range(1,len(nums)-1):
    if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
      result.append(nums[i])
  return len(result)
  

print(greater_than_neigbors([1, 5, 1, 5 , 1])) # 2 



# def greater_than_neigbors2(a)

#   counter = 0
#   for i in range(1, len(a) - 1):
#     if a[i - 1] < a[i] > a[i + 1]:
#       counter += 1
#   print(counter)

#   a = [int(s) for s in input().split()]
#   print(greater_than_neigbors2(a))