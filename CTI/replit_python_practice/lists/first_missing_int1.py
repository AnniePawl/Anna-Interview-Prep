# Given a sorted int array, first first missing positive int 
# Should run in O(n) time 

def first_missing(a):
  if a[-1] < 0:
    return 1 
  for i in range(len(a)-1):
    if a[i] > 0 and a[i+1] - a[i] > 1:
      return a[i] + 1
  return a[-1] +1
      
    

print(first_missing([0,1,2])) # 3 
print(first_missing([-1,1,3,4])) # 2 
print(first_missing([-8,-7,-6])) # 1 
print(first_missing([1, 2, 2, 3, 4, 5, 7, 8])) # 6


