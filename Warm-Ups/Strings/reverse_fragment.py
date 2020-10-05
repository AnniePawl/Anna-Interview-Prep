# Given string with at least 2 occurances of h, reverse the string fragment between first and last 

def reverse_fragment(str):
  first_h = str.find('h')
  last_h = str.rfind('h')
  return str[:first_h] + str[first_h:last_h][::-1] + str[last_h:]

print(reverse_fragment("In the hole in the ground there lived a hobbit"))
# In th a devil ereht dnuorg eht ni eloh ehobbit


 