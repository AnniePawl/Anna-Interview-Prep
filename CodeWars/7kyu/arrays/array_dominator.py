# Return value that dominates (occurs most) in array. If no dominator, return -1
from collections import Counter 

# This function doesnt return -1 
def dominator(array):
  return max(set(array), key= array.count)


# Using imported Counter
def dominator2(array):
  count_dict = Counter(array)
  return max(count_dict)




print(dominator([1,2,3,4,5])) # -1 (b/c no dominator)
print(dominator([1,1,2,3,1,1,])) # 1 
print(dominator([4,5,5,6,5,7,5])) # 5 (b/c no dominator)


print(dominator2([1,2,3,4,5])) # -1 (b/c no dominator)
print(dominator2([1,1,2,3,1,1,])) # 1 
print(dominator2([4,5,5,6,5,7,5])) # 5 (b/c no dominator)