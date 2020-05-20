# Return total sum or each element in array squared 

def squared_sum(nums):
  sum = 0 
  for num in nums:
    sum += num ** 2
  return sum

def squared_sum2(nums):
  return sum(num ** 2 for num in nums)



print(squared_sum([1,1,2])) # 6
print(squared_sum([2,2,4])) # 24


print(squared_sum2([1,1,2])) # 6
print(squared_sum2([2,2,4])) # 24