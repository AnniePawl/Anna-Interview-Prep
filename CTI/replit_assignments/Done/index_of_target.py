# Given array of sorted ints, return starting and ending index or target num. If target not found, return [-1,-1]

def index_of_target(arr, target):
  if arr.count(target) == 0:
    return [-1,-1]
  else:
    return [arr.index(target), (len(arr)-1) - arr[::-1].index(target)]


print(index_of_target([5,7,7,8,8,10], 8)) # [3,4]
print(index_of_target([5,7,7,8,8,10], 11)) # [-1,-1]


# CTI SOLUTION 
def search_for_range(array, target):
  
  # perform a binary search that searches to the left when target has been found
  # the resulting index will always be the target's starting index
  lo, hi = 0, len(array)
  while lo < hi:
      mid = (lo + hi) // 2
      if array[mid] > target:
          hi = mid
      elif array[mid] == target:
          hi = mid
      else:
          lo = mid + 1
  start = hi
  # if the target is not in this array, return failure indices
  if array[start] != target: return [-1, -1]
  
  # perform a binary search that searches to the right when target has been found
  # the resulting index will always be the target's end index
  lo, hi = 0, len(array)
  while lo < hi:
      mid = (lo + hi) // 2
      if array[mid] > target:
          hi = mid
      elif array[mid] == target:
          lo = mid + 1
      else:
          lo = mid + 1
  end = hi - 1
  
  return [start, end]