# 16. Remove all chars except ints from string 

def remove_alpha(s):
  return ''.join([char for char in s if char.isdigit()])

print(remove_alpha('I am 27 and 10 months'))
# 2710