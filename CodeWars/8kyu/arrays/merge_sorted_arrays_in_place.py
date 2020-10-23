# Given 2 sortd arrays, merge nums2 into nums1
# Don't return new arrays, instead modify nums1 in place


#  Inefficient Solution 
def merge(arr1,arr2):
  new_array = arr1 + arr2
  return sorted(new_array)

print(merge([1,2,3,0,0,0], [2,5,6])) # [1,2,2,2,3,5,6]


# def merge_arrays(a,b):
#   # CTI SOLUTUION 
# def merge_sorted_list(nums1, nums2):
#   nums1_index = 0
#   nums2_index = 0
  
#   while nums2_index < len(nums2):
#     if nums2[nums2_index] <= nums1[nums1_index] or nums1[nums1_index] == 0:
#       # insert nums2[nums2_index] into nums1[nums1_index]
#       nums1.insert(nums1_index, nums2[nums2_index])
#       # remove an element at the end of the list
#       nums1.pop()
#       nums2_index += 1
#     else:
#       nums1_index += 1


  


# print(merge_arrays([1,3,5], [2,4,6])) #[1,2,3,4,5,6]
# print(merge_arrays([2,4,8], [2,4,6])) #[2,4,6,8]