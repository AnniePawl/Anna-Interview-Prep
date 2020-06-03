# Cupcake costs a dollars and b cents. Return hwo many dollars and cents needed to by c cupcakes. 

def cupcakes(a,b,c):
    dollars = a*c
    cents = b*c
    if cents > 100:
      dollars += cents //100
      cents = cents % 100
  
    return str(dollars) + " " + str(cents)

print(cupcakes(10,15,2)) # 20 30
print(cupcakes(2,50,4)) # 10 0 