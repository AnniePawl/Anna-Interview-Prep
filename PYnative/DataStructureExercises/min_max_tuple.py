# Remove duplicates from list. 
# Create Tuple
# Find min and max 

def min_max_tuple(nums):
  unique_items = set(nums)
  print("Unique Items: " + str(unique_items))
  unique_tuple = tuple(unique_items)
  print("Unique Items Tuple: " + str(unique_tuple))
  print("Min: " + str(min(unique_tuple)))
  print("Max: " + str(max(unique_tuple)))
  
print(min_max_tuple([87, 45, 41, 65, 94, 41, 99, 94]))
