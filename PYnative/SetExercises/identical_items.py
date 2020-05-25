# Return identical values from 2 sets 
# Use .intersection() to find overlapping values

def identical_values(set1,set2):
  identical = set1.intersection(set2)
  return identical

set1 = {10,20,30,40,50}
set2 = {20,30,60,70,80}
print(identical_values(set1,set2)) # {20,30}