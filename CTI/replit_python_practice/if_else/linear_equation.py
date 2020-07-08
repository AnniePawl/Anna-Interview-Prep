# Solve linear equaton ax = b 
# a may be 0 
# Print single integer root if it exists 
# Print "no solution" or "many solutions" otherwise

def linear_equation(a,b):
  if a == 0:
    if b == 0:
      print('many solutions')
    else:
      print('no solution')
  elif b % a == 0:
    print(b // a)
  else:
    print('no solution')

print(linear_equation(1,-2)) # -2
print(linear_equation(2,-1)) # no solution
print(linear_equation(0,0)) # many solutions
