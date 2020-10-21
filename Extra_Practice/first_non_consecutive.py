# Find the first non consecutive element of an array (first not exactly 1 larger than previous element in array). If the wold array is consecutive, return null 


# Method One
def first_non_consecutive(arr):
  for i in range(len(arr)-1):
   if arr[i+1] - arr[i] != 1:
     return arr[i+1]
  else:
    return null

    

print(first_non_consecutive([1,2,3,4,6,7,8])) # 6


# Method Two (using enumerate)
def non_consecutive(arr):
  for i, j in enumerate(arr):
    if j+1 != arr[i+1]:
      return arr[i+1]
  return None

print(non_consecutive([1,2,3,4,5,7])) #7