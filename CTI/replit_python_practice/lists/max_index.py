# Given list of ints, find first max elements, return it and its index

def max_index(nums):
  max_num = max(nums)
  index =  nums.index(max(nums))

  print(max_num, index, end = " ")

print(max_index([1,2,3,2,1])) # 3,2 
