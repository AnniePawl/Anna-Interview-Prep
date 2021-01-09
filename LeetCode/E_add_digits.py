# Given non-neg integer, repeatedly add digits until result has only 1 digit 
# Try in O(1) runtime 

def add_digits_iterative(num):
  print (num % 10)


def add_digits_recursive(num):
  pass 
  
print(add_digits_iterative(38)) # 2 
# 3 + 8 = 11, 1 + 1 = 2
print(add_digits_recursive(38)) # 2 


# How to split number into seperate digits 
# Convert int to string 
# Use list comprehension to split into individual digits
# return [n for n in str(num)]