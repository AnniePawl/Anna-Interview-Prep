#  Sort a vector of strings. Then return first value with three "*" between each letter 


# Jankny Way
def sort_star(array):
  sorted_array =  sorted(array) 
  result = ""
  for letter in sorted_array[0]:
    result += letter + "***"
  return result[:-3]
  
def sort_star2(array):
  return "***".join(min(array))



print(sort_star(["i", "love", "code"])) # c***o***d***e
print(sort_star(["gum", "ball"])) # b***a***l***l

print(sort_star2(["i", "love", "code"])) # c***o***d***e
print(sort_star2(["gum", "ball"])) # b***a***l***l