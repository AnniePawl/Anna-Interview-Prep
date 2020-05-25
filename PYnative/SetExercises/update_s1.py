# Update set1 by adding items from set 2, excpet common items 

def update(set1,set2):
  set1.symmetric_difference_update(set2)
  return set1

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
print(update(set1,set2)) # {1,2,6,7}