# Return True if all chars in s1 are also in s2. Char position doesn't matter 

def balanced_string(s1,s2):
  return s1 in s2

print(balanced_string("py", "python")) # True 
print(balanced_string("doom", "grubby")) # False
print(balanced_string("ana", "banana")) # True 