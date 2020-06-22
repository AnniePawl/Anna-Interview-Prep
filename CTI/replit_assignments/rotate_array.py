# Given an array, rotate it right by k steps

def rotate_array(arr, k):
   return arr[k:] + arr[:k]


print(rotate_array([1,2,3,4,5,6,7], 3)) # [5,6,7,1,2,3,4]

print(rotate_array([-1,-100,3,99],2)) # [3,99,-1,-100]