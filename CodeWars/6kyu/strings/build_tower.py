# Built a tower out of "*" given number of floors 
# Patterns - starts w/ 1 star, each floor increases by 2 stars

def build_tower(floors):
  result = []
  star_count = 1
  bottom_count = (floors * 2) -1
  for i in range(floors):
    result.append( (bottom_count - star_count)  * " " + star_count * "*" + (bottom_count - star_count) * " ")
    star_count += 1
  return result



print(build_tower(1)) 
# [
#   '*',  
# ]

print(build_tower(2)) 
# [
#   ' * ', 
#   '***', 
# ]

print(build_tower(3)) 
# [
#   '  *  ', 
#   ' *** ', 
#   '*****', 
# ]

