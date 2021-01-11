# Split string at hyphens and return each substring on new line 

def split(s):
  s = s.split('-')
  return '\n'.join(s)
  

print(split('Emma-is-a-data-scientist'))