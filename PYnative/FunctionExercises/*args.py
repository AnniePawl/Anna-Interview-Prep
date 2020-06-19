# accept two variables, name and age. Print them 
# use *args - special syntax to pass a variable number of arguments into a function. 

def name_age(*args):
  for item in args:
    print(item)

print(name_age("Kit", 22))