# N nums given in input, print their sum 
# Fist line contains num of integers 

a1 = int(input())
nums = []
for i in range(a1):
  nums.append(int(input()))
print(sum(nums))


# Solution 2 
result = 0
for i in range(int(input())):
  result += int(input())
print(result)


