# Given 2 sets, find intersection and remove those elements from first set 

def remove_intersection(set1, set2):
  intersection = set1.intersection(set2)
  for item in intersection:
    set1.remove(item)
  return set1

print(remove_intersection({65,42,78,83,23,57,29}, {67,73,43,48,83,57,29})) 
# Intersection is {57,83,29}
# New set1 is {65,42,78,23}