# Solve linear equaton ax = b 
# a may be 0 
# Print single integer root if it exists 
# Print "no solution" or "many solutions" otherwise

def linear_equation(a,b):
  if a == 0  and b == 0:
    return("many solution")
  elif a == 0 and b != 0:
    return("no solution")
  elif (b / a ) % 2 == 0:
    return (b // a)
  else: 
    return("no solution")
      



print(linear_equation(1,-2)) # -2
print(linear_equation(0,0)) # many solutions
