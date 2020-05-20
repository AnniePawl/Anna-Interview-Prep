# Count number of lowercase letters in string 

def lower_count(string):
  return sum(1 for char in string if char.islower())

print(lower_count("abc123")) #3 
print(lower_count("Geasy!")) #4 
 