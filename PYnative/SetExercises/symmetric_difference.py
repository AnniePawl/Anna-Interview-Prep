# Return set of all elements in either A or B , but not both 

def symmetric_difference(set1,set2):
  return set1.symmetric_difference(set2)




set1 = {1,2,3,4,5}
set2 = {2,3,4,6}
print(symmetric_difference(set1, set2)) # {1,5,6}