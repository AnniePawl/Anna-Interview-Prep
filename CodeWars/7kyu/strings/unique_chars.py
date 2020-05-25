# Given string a and b, return characters not shared in both string 


# Brute Force 
def unique_chars(a,b):
  new_string = ""
  for char in a:
    if char not in b:
      new_string += char 
  for char in b:
    if char not in a:
      new_string += char
  return new_string


# One-liner
def unique_chars2(a,b):
  return "".join([c for c in a if not c in b] + [c for c in b if not c in a])


# Using Sets 
def unique_chars3(a,b):
  s = set(a)&set(b)
  return "".join(c for c in a + b if c not in s)


print(unique_chars("xyab", "xzca")) #ybzc
print(unique_chars("xxx", "xa")) #a
print(unique_chars2("xyab", "xzca")) #ybzc
print(unique_chars2("xxx", "xa")) #a
print(unique_chars3("xyab", "xzca")) #ybzc
print(unique_chars3("xxx", "xa")) #a