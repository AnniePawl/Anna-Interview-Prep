# replace all punctuation with # 

from string import punctuation

def replace_punctuation(s):
  for char in punctuation:
    s = s.replace(char, '#')
  return s

print(replace_punctuation('/*Jon is @developer & musician!!'))
##Jon is #developer # musician##