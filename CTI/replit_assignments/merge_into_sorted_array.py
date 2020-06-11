# Given two sorted int arrays, merge them into one sorted array. 

def sorted_merge(nums1, nums2):
  return sorted(nums1 + nums2)

print(sorted_merge([1,2,3,0,0,0], [2,5,6]))
# [1,2,2,3,5,6]