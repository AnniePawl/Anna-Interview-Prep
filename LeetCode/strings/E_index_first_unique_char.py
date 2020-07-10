# Given a string, return index of first non-repeating char. 
# If no non-repeating char, return -1

def index_unique(s):
  for char in s:
    if s.count(char) == 1:
      return s.index(char)
  return -1
    
     

print(index_unique("anna")) # -1
print(index_unique("leetcode")) # 0
print(index_unique("lovely")) # 1