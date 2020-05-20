# Given a list of ages, return tuple with youngest, oldest, and difference between the two 

def age_difference(ages):
  return (min(ages), max(ages), max(ages)-min(ages))

print(age_difference([12,76,49,3,38,84,23])) # (3,84,81)
