# Given 5 numbers, iterate over each and print sume or current number and previous number

def consecutive_sums(nums):
  for i in range(len(nums)):
    print(nums[i] + nums[i-1])

print(consecutive_sums([0,1,2,3,4,5,6,7,8,9])) # 1, 3, 5, 7
