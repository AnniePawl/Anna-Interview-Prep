# Output a string w/ comma delimited elements of array in same order 

def add_commas(arr):
  return ",".join(map(str,arr))

def add_commmas2(arr):
  return ",".join(str(a) for a in arr)


print(add_commas(["Hi", "I'm", "Paul"])) # ["Hi, I'm, Paul"]
print(add_commas([4,5,6])) # ["4,5,6"]


print(add_commas2([4,5,6])) # ["4,5,6"]