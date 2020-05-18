# Remove empty string from list of strings 

def remove_empty(list1):
  return list(filter(None, list1))

print(remove_empty(["a", "b", "", "d"]))