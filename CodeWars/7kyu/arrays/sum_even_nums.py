# Return sum of even values in sequence 

def sum_evens(nums):
  sum = 0 
  for num in nums:
    if num % 2 == 0 :
      sum += num 
  return sum 

def sum_evens2(nums):
  return sum(num for num in nums if num % 2 == 0)

print(sum_evens([1,2,3,4,5,6,7,8,9,10])) # 30
print(sum_evens([10,11,12,13])) # 22
print(sum_evens([])) # 0

print(sum_evens2([1,2,3,4,5,6,7,8,9,10])) # 30
print(sum_evens2([10,11,12,13])) # 22
print(sum_evens2([])) # 0