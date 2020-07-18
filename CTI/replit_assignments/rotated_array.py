# Suppose sorted array A is rotated at some unknown pivot. Find the minumum element. Array will not contain duplicates. Do not use sort. Figure out how many times array was rotated 

# Linear Search O(n) - we can just search array to find min - try different approach 

# Binary Search O(nlogn) 
# Number of rotations also = min element 
# Items are circularly sorted 
# PIVOT PROPERTY - Notice that pivot point is only point where BOTH values before and after it are greater than it 

def min_of_rotated_array(A):
  rotations = 0 
  next = (mid+1) % n 
  previous = (mid+n-1) % n
  
  
# This is called a circularly sorted array
print(min_of_rotated_array([4,5,6,7,0,1,2])) # 0
print(min_of_rotated_array([11,12,15,18,2,5,6,8])) # 2