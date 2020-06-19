# Reverse list of ints using for loop 

def reverse_list(nums):
  reversed_nums = []
  for i in range(len(nums)-1, -1, -1):
    reversed_nums.append(nums[i])
  return reversed_nums


print(reverse_list([10,20,30,40,50])) # [50,40,30,20,10]