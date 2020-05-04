# Return middle character of word. If word length is even, return middle 2 characters 

def get_middle(s):
  if len(s) == 2:
    return s
  # if word even
  elif len(s) % 2 == 0:
    return s[(len(s)//2)-1: (len(s)//2) +1]
  else:
    return s[len(s)//2]

# Condensed version
def get_middle_v2(s):
  rturn s[(len(s)-1)/2: len(s)/2+1]

print(get_middle('bob')) # b
print(get_middle('bboobb')) # oo
print(get_middle('joey')) # oe
print(get_middle('grettle')) # t
print(get_middle('A')) # A
print(get_middle('of')) # of