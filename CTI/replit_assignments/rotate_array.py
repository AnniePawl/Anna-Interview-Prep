# Given an array, rotate it right by k steps
# Do not return new array, instead modify array in place

def rotate_array(arr, k):
  rotations = k
  while rotations > 0:
    last = arr.pop()
    arr.insert(0,last)
    rotations -=1
  return(arr)


def rotate_array2(arr,k):
  for x in range(1,k+1):
    end = arr.pop()
    arr.insert(0, end)

print(rotate_array([1,2,3,4,5,6,7], 3)) # [5,6,7,1,2,3,4]
print(rotate_array([-1,-100,3,99],2)) # [3,99,-1,-100]