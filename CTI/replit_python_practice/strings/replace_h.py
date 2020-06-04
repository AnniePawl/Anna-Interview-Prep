# Given a string,  replace all lowercase "h" with "H" except first and last one


def replace_h(str):
  # Indices of 1st and last h 
  first_h = str.find('h')
  last_h = str.rfind('h')
  # print(first_h)
  # print(last_h)

  str[first_h +1: last_h].replace('h', "H")
  return str
  

print(replace_h("how hot and happy is henry")) # how Hot and Happy is henry