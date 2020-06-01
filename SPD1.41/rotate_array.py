# Given an array (a), write funnction that executes n left rotations on array. 

# Time Compelxity: 
def rotate_left(array, n):
  return array[n:] + array[:n]


array = [1,2,3,4,5]
print(rotate_left(array, 1)) # [2,3,4,5,1]
print(rotate_left(array, 3)) # [4,5,1,2,3]