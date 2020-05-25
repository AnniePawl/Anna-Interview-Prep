# Remove 10, 20, and 30 from following set at one time 

def remove_elements(set1):
  set1.difference_update({10,20,30})
  return set1

print(remove_elements({10,20,30,40,50})) # {40,50}