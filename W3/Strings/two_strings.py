# 68. Create two strings from given string. First string using cahrs that only occur once, second string from chars that occur multiple times 
def two_strings(s): # O(n^2)
  singles = ''
  dups = ''
  for char in s.replace(' ', ''): # O(n)
    if s.count(char) == 1: # O(n)
      singles += char
    else:
      if char in dups: # O(n)?
        continue 
      else:
        dups += char 

  return singles, dups

def two_strings2(s):
  counts = {}
  for char in s.replace(' ',''): # O(n)
    if char in counts: # 0(1) to check if key in dict 
      counts[char] += 1
    else:
      counts[char] = 1

  singles = ''
  doubles = ''
  for key, value in counts.items():
    if value == 1:
      singles += key
    else:
      doubles += key
      
  return (singles, doubles)



print(two_strings('apple bottom jeans')) # 'lbmns' 'apeto'
print(two_strings2('apple bottom jeans')) # 'lbmns' 'apeto'