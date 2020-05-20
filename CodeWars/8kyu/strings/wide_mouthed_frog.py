# Take in argument (animal) which corresponds to animal that frog encountered. If animal is alligator(case sensative), return "small" otherwise return "wide"

def mouth_size(animal):
  if animal.lower() == "alligator":
    return "small"
  else:
    return "wide"

# one-liner
def mouth_size2(animal):
  return "small" if animal.lower() == "alligator" else "wide"
