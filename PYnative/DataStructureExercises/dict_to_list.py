# Given a dictionay, get all values and add to list, exclude duplicates 

def dict_to_list(dict):
  value_list = []
  for key in dict:
    if dict[key] not in value_list:
      value_list.append(dict[key])
  return value_list
    

print(dict_to_list({'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54})) 
#  [47, 52, 44, 53, 54]


def dict_to_list2(dict):
  speed_list = list()
  for item in dict.values():
    if item not in speed_list:
      speed_list.append(item)
  return speed_list


print(dict_to_list2({'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54})) 
#  [47, 52, 44, 53, 54]