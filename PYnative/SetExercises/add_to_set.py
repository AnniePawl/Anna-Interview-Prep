# Add list of elements to an existing set 

# Use ".update()" to add multiple values to set 

def add_to_set():
  set1 = {"Yellow", "Orange", "Black"}
  list1 = ["Blue", "Green", "Red"]
  set1.update(list1)
  return set1

print(add_to_set())
