# A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes. A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.


def total_cost(a,b,c):
  dollars = a * c 
  cents = b * c 
  if cents >= 100:
    dollars += cents // 100
    cents = cents % 100
  print(dollars, cents)

print(total_cost(10,15,2)) # 20 30
print(total_cost(10,99,7)) # 76 93