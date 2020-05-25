# Determine if sets have common elements. If so, return 

def common(set1,set2):
   return set1.intersection(set2)


set1 = {1,2,3}
set2 = {2,3,4}
print(common(set1,set2)) # {2,3}