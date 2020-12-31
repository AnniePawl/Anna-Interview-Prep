# Concatenate two lists by index 

def concatenate(list1, list2):
  return [i + j for i,j in zip(list1, list2)]

print(concatenate(["H","C"], ["oly", "ow"])) # Holy Cow
print(concatenate(["a","c"], ["b", "d"])) # abcde


def contcat(list1,list2):
  return [i + j for i,j in zip(list1,list2)]
  
print(contcat( ["M", "na", "i", "Ke"],["y", "me", "s", "lly"]))