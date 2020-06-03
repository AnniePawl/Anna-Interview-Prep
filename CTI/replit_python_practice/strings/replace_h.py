# Given a string,  replace all lowercase "h" with "H" except first and last one


def replace_h(str):
  # Indices of 1st and last h 
  first_h = str.find('h')
  last_h = str.rfind('h')

  for char in str[first_h +1, last_h]:
    char.replace('h', "H")
  
  

print(replace_h("how hot and happy is henry")) # how Hot and Happy is henry