# Given two arrays, determine if both contain exactly the same elements, regardless of order 

# Boolean, return True or False? 

# Sort method 
# Time complexity:  0(n log n) ? 
# Space complexity: O(n)
def same_values(arr1, arr2):
  return sorted(arr1) == sorted(arr2)

# Hash method - reduce and map
# Time complexity: 0(n)
# Space complexity: O(n)



print(same_values([1,2,3], [2,3,1])) # True 
print(same_values([1,2,3], [1,2,4])) # False 
