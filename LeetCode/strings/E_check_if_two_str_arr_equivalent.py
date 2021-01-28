# Given two string arrays, return True if they represent the same string(array elements concatonated in order form the string)

def string_equ(s1,s2):
  return ("".join(x for x in s1)) == ("".join(x for x in s2))




print(string_equ(['ab','c'], ['a','bc'])) # True
print(string_equ(['ac','b'], ['a','bc'])) # False
print(string_equ(["abc", "d", "defg"], ['a'])) # False