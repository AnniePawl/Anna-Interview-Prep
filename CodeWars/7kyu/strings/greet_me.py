# Take in name and greet 


def greet(name):
  return "Hello " + name.capitalize() + "!"

# Using format 
def greet2(name):
  return f'Hello {name.title()}!'

print(greet2("nancy"))
print(greet("nancy"))