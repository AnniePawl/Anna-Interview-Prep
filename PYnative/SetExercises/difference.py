# Given 2 sets, update first set with items that exists only in first set but not in second 

def difference(set1,set2):
  set1.difference_update(set2)
  return set1
  

set1 = {10,20,30}
set2 = {20,40,50}
print(difference(set1,set2)) # {10,30}