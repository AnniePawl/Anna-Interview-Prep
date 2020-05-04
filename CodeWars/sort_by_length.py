# Take in array of strings, and returns array ordered from shortest to longest 

def sort_by_length(arr):
  return sorted(arr, key = lambda e: len(e))
    

print(sort_by_length(["doggy", "parrot", "cat"])) # ["cat", "doggy", "parrot"]
print(sort_by_length(['bb', 'ccc', 'a']))