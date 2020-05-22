# Given 2D array, find sum of min val in each row 

def sum_mins(nums):
  mins = []
  for sub_list in nums:
    mins.append(min(sorted(sub_list)))
  return sum(mins)

def sum_mins2(nums):
  return sum(min(sorted(sub_list)) for sub_list in nums)
  

# Use MAP for most efficient solution
def sum_mins3(nums):
  return sum(map(min, numbers))


print(sum_mins([[2,1,3], [6,5,4], [8,7,9]])) #12
print(sum_mins2([[2,1,3], [6,5,4], [8,7,9]])) #12

