# Given 5 numbers, iterate over each and print sume or current number and previous number

def consecutive_sums(nums):
  previous_num = 0
  for i in range(len(nums)):
    sum = previous_num + i
    print(sum)
    previous_num= i

print(consecutive_sums([1,2,3,4])) # 1, 3, 5, 7
