# Given a string with at least 2 occurances of "h" remove fragment between and including first and last h


def remove_fragment(str):
  first_h = str.find('h')
  last_h = str.rfind('h')
  return str[:first_h] + str[last_h+1:]


print(remove_fragment("In the hole in the ground there lived a hobbit"))

# In tobbit