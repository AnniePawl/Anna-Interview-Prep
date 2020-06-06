# Given string where 'h' occurs at least 2x, remove first and last occurance as well as everything in between 

def remove_chunk(s):
  first_h = s.find('h')
  last_h = s.rfind('h')
  return s[:first_h] + s[last_h+1:]

print(remove_chunk('a happy hippo')) # a ippo