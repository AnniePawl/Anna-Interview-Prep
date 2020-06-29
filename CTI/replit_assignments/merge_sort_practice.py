# Problem: Given list of unsorted numbers, sort them using "merge sort" algorithm Don't use built-in .sort() or sorted()
# Merge sort is usually done recursively 
# Divide in conquer  - continuously break array in half  

# Strategy 
# Merge left half
# Merge right half 
# Merge left and right in sorted order

# Time Complexity: O(nlogn)
# Space Complexity: 0(n)
def merge_sort(nums):
  merge_sort2(nums, 0, len(nums)-1)

def merge_sort2(nums, first, last):
  if first < last: # if more than one item in list.. 
    middle = (first + last) //2 
    merge_sort2(nums, first, middle) # call of list 1st half
    merge_sort2(nums, middle + 1, last) # call on list 2nd half
    merge(nums, first, middle, last) # combines both sorted lists 

def merge(nums, first, middle, last):
  left = nums[first:middle] # left half of list 
  right = nums[middle:last+1] # right half of list
  i = j = 0 # initialize left and right half index

  for k in range(first, last + 1):
    if left[i] <= right[j]:
      nums[k] = left[i]
      i +=1
    else:
      nums[k] = right[j]
      i +=1


print(merge_sort([3,5,9,2,6,1])) #[1,2,3,5,6,9] 