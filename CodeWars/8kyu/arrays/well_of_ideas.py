# Check array for good and bad ideas. If 1 or 2 good, return "Publish!", if more than 2 return "I smell a series!" If no good ideas, return "Fail"

def well_ideas(array):
  if array.count("good") > 2:
    return "I smell a series"
  if array.count("good") >=1<2:
      return "Publish!"
  else:
    return "Fail!"


def well_ideas2(x):
  c = x.count("good")
  return "I smell a series!" if c > 2 else "Publish!" if c else "Fail!"


print(well_ideas(["bad", "bad", "bad"])) # Fail! 
print(well_ideas(["good", "bad", "bad"])) # Publish! 
print(well_ideas(["good", "good", "good"])) # I smell a series

print(well_ideas2(["bad", "bad", "bad"])) # Fail! 
print(well_ideas2(["good", "bad", "bad"])) # Publish! 
print(well_ideas2(["good", "good", "good"])) # I smell a series! 