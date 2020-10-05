# Given a string with multuple 'h's, replace all except first and last with "H"


def replace_h(str):
  first_h, last_h = str.find('h'), str.rfind('h')
  left, middle, right = str[:first_h+1], str[first_h+1:last_h], str[last_h:]
  return left + middle.replace('h','H') + right
  
  
print(replace_h("hi holly how hairy is she"))
# hi Holly How Hairy is she