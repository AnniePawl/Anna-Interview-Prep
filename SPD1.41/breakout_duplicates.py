# Does List Contain Duplicates ? True or False 

# Stategy one: .count() method
# Time complexity: O(n^2)
def duplicates_count(arr):
  for num in arr:
    if arr.count(num) > 1:
      return True 
  return False

print(duplicates_count([1,2,3,4,5])) # False 
print(duplicates_count([1,2,3,4,5,2])) # True


# Strategy Two: set() and len()
# Time Complexity: O(nlogn)
def duplicates_set(arr):
  if len(arr) == len(set(arr)):
    return False 
  return True
  
print(duplicates_set([1,2,3,4,5])) # False 
print(duplicates_set([1,2,3,4,5,2])) # True

