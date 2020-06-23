# Return average of sequence of ints written on seperate lines and ending in 0 

a = int(input())
nums = []
while a != 0:
  nums.append(a)
  a = int(input())
print(sum(num for num in nums) / len(nums))