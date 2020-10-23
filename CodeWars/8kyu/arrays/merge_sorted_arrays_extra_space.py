# Given 2 sorted arrays, merge them into a new sorted array 


def merge_arrays(arr1,arr2):
  new_array = []
  i = 0 
  j = 0
  # Compare value at each pointer 
  while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
      new_array.append(arr1[i])
      i +=1 
    else:
      new_array.append(arr2[j])
      j +=1 

  while i < len(arr1):
    new_array.append(arr1[i])
    i +=1 
  while j < len(arr2):
    new_array.append(arr2[j])
    j +=1

  return new_array
 


print(merge_arrays([1,3,5], [2,4,6])) # [1,2,3,4,5,6]
print(merge_arrays([2,4,8], [2,4,6,8,12,13])) # [2,2,4,4,6,8,8,12,13]

