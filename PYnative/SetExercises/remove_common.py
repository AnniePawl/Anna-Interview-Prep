# Remove items from set1 that are not common in both sets 

def remove_common(set1,set2):
  set1.intersection_update(set2)
  return set1

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
print(remove_common(set1, set2)) # {3,4,5}