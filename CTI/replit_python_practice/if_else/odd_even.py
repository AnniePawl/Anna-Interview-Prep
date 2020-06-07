# Given an int, print "odd" or "even"

def even_odd(num):
  if num % 2 == 0:
    return "even"
  else:
    return "odd"

print(even_odd(5)) # odd
print(even_odd(8)) # even