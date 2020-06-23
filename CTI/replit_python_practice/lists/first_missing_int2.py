# Given an UNsorted array, find first missing positive integer 
# Should run in O(n^2) time

def first_missing(a):
  a.sort() #(n log n)
  if a[-1] < 0:
    return 1 
  for i in range(len(a)-1): # O(n)
    if a[i]> 0 and a[i+1] - a[i] > 1:
      return a[i] +1
  return a[-1] + 1


print(first_missing([0, 2, 1])) # 3
print(first_missing([-1,4, 1,3])) # 2
print(first_missing([-8, -9, -6])) # 1
print(first_missing([4, 2, 2, 3, 5, 1, 8, 7] )) # 6