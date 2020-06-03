# Count how many unique value in array 

def unique_count(nums):
  return sum(1 for x in set(nums))

def unique_count2(nums):
  return len(set(nums))

print(unique_count([1,2,3,2,1])) # 3
print(unique_count2([1,2,3,2,1])) # 3