# Find needle in array, return index

def find_needle(arr):
  return "found needle at position: " + str(arr.index("needle"))

print(find_needle(['button', 'grass', 'fluff', 'needle', 'bob'])) # 3

print(find_needle(['needle','dood', 'fish'])) # 0