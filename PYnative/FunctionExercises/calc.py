# Accept 2 variables and return sum and difference 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def calc(a,b):
  print("The sum of your numbers is: " + str(a+b))
  print("The difference of your numbers is: " + str(a-b))

print(calc(a,b))