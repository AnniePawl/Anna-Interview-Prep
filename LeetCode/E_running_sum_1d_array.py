# Given an array num return the running nsum 
# runningnSum[i] = sum(nums[0]...num[i])

def running_sum(nums):
  return [sum(nums[:i+1]) for i in range(len(nums))]

def running_sum2(nums):
  next_sum = 0
  for i, num in enumerate(nums):
    next_sum += num
    # print(next_sum)
    nums[i] = next_sum
  return nums
    
def running_sum3(nums):
  running_sum = [nums[0]]
  prev = nums[0]
  for i in range(len(nums)-1):
    running_sum.append(nums[i+1]+ prev)
    prev = running_sum[i+1]
  return running_sum


print(running_sum([1,2,3,4]))
# [1,3,6,10]
# Explaination: [91, 1+2, 1+2+3, 1+2+3+4]
print(running_sum([3,1,2,10,1])) # [3,4,6,16,17]

print(running_sum2([3,1,2,10,1])) # [3,4,6,16,17]

print(running_sum3([3,1,2,10,1])) # [3,4,6,16,17]