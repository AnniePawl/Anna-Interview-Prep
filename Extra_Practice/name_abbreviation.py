# Abbreviate a two word name 

# Method One 
def abbreviate(str):
  split_str=str.split()
  return split_str[0][0].upper() + "." + split_str[1][0].upper()

print(abbreviate("sam smith")) #S.H

# Method Two 
def abb(str):
  return ".".join(word[0] for word in str.split()).upper()

print(abb("Henry ford")) # H.F