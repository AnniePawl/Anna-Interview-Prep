# Solve equation ax = b 
# Print single integer root or "no solution" / "many solutions" otherwise 

def linear_equation(a,b):
  if a == 0 :
    return "many solutions"
  elif (b / a ) % 2 == 0:
    return b // a
  else: 
    return "no solution"
   

print(linear_equation(1,-2)) # -2
print(linear_equation(0,-2)) # "many solutions"
print(linear_equation(2,-1)) # "no solution"
print(linear_equation(0,7)) # "many solutions"