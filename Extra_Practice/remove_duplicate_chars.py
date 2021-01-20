#  Remove duplicate chars from a string 


def remove_duplicates(str):
  # Method 1: Use set --> if order doenst matter
  # return ''.join(set(str))
  # Method 2: Dict --> if order matters 
  return ''.join((dict.fromkeys(str)))


print(remove_duplicates('butter ball')) #buter al