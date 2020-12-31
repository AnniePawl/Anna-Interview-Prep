# Given an int, return int w/ reversed digits
# It can be positive or negative 

def reverse_int(x):
  # account for possible negative
  string_x = str(x)
  if string_x[0] == '-':
    return int("-"+string_x[:0:-1])
  else:
    return int(string_x[::-1])
  

print(reverse_int(-231)) # -132
print(reverse_int(345)) # 543s