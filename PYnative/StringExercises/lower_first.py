# Arrange string characters so lowercase letters come first 

def lower_first(str):
  lower_string = []
  upper_string = []

  for char in str:
    if char.islower():
      lower_string.append(char)
    else:
      upper_string.append(char)

  return "".join(lower_string+upper_string)

print(lower_first("AnnaMillicentPawl")) #nnaillicentawlAMP
print(lower_first("BBBccc")) #cccBBB