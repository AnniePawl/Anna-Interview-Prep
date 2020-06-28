# Given two sorted int arrays, merge nums2 into nums1 are one sorted array 

def sorted_merge(nums1, nums2):
  # nums1 = [num for num in nums1 if num != 0]
  while 0 in nums1:
    nums1.remove(0)
  while 0 in nums2:
    num2.remove(0)
  
  nums1.extend(nums2)
  nums1.sort()
  return nums1

print(sorted_merge([1,2,3,0,0,0,0,0], [2,5,6]))



# CTI SOLUTUION 
def merge_sorted_list(nums1, nums2):
  nums1_index = 0
  nums2_index = 0
  
  while nums2_index < len(nums2):
    if nums2[nums2_index] <= nums1[nums1_index] or nums1[nums1_index] == 0:
      # insert nums2[nums2_index] into nums1[nums1_index]
      nums1.insert(nums1_index, nums2[nums2_index])
      # remove an element at the end of the list
      nums1.pop()
      nums2_index += 1
    else:
      nums1_index += 1



# First Try
# Works, but doesn't modify nums1 in place
def sorted_merge2(nums1, nums2):
  nums1.extend(nums2)
  nums1 = sorted(nums1)
  return [num for num in nums1 if num !=0]
