#  Return 2 highest values in list. Don't include duplicates

def return_highest(nums):
  return [sorted(set(nums))[-1], sorted(set(nums))[-2]]

print(return_highest([4,10,10,9,2])) # [10,9]
print(return_highest([24,10,43,43,2])) # [10,9]