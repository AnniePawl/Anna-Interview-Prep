# 10 ints given as input, return their sum 

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# f = int(input())
# g = int(input())
# h = int(input())
# i = int(input())
# j = int(input())

def sum(nums):
  sum = 0
  for num  in nums:
    sum += num
  return sum

def sum2(nums):
  return sum(nums)

def sum3(nums):
  result = 0
  for i in range(10):
    result += int(input())
  return result
    
  
print(sum([0,1,2,3,4,5,6,7,8,9])) #45
print(sum2([0,1,2,3,4,5,6,7,8,9])) #45

