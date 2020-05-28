#  Given list of ints, and n- return nth smallest element 

def nth_smallest(nums, n):
  return sorted(nums)[n-1]

print(nth_smallest([3,4,2,5,6,7,1], 2)) # 2 
print(nth_smallest([8,6,2,3,1,9], 4)) # 6 