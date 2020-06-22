# Return new array with duplicate items 

def duplicates(arr):
  duplicates = []
  for item in arr:
    if arr.count(item) > 1 and item not in duplicates:
      duplicates.append(item)
  return duplicates

print(duplicates([1, 2, 4, 4, 3, 3, 1, 5, 3, '5'])) # [1,4,3]
print(duplicates([1,2,3,4,5])) # []

def duplicates2(arr):
  duplicates = []
  seen= []
  for item in arr:
    if item in seen and item not in duplicates:
      duplicates.append(item)
    seen.append(item)
  return duplicates

 
# Keep items in order 
print(duplicates2([1, 2, 4, 4, 3, 3, 1, 5, 3, '5'])) # [4,3,1]