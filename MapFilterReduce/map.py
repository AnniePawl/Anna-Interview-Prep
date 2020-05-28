# map() function returns object after applying given function to each item in iterable 
# map(function, interable)

def addition(n):
  return n + n 

nums = (1,2,3,4)
print(map(addition, nums))