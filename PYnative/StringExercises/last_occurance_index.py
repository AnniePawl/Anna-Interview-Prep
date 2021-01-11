# Find last position of substring "Emma"

def last_occurance(s):
  return s.rindex('Emma') # throws error if not found
  # return s.rfind('Emma')

print(last_occurance("Emma is a data scientist who knows Python. Emma works at google."))