# Merge two sorted arrays. Final outcome must be sorted w/ no duplicates 


def merge_arrays(a,b):
  return sorted(set(a+b))



print(merge_arrays([1,3,5], [2,4,6])) #[1,2,3,4,5,6]
print(merge_arrays([2,4,8], [2,4,6])) #[2,4,6,8]