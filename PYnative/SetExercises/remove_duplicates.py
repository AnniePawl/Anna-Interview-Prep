# Return new set with items from both sets, removing duplicates 

def remove_duplicates(set1,set2):
  return set1.union(set2)

set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
print(remove_duplicates(set1, set2))