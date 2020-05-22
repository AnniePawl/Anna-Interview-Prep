# Return array of two oldest ages 

def oldest_ages(ages):
  return sorted(ages)[-2:]

print(oldest_ages([50,23,61,34,91,5])) #[62,91]