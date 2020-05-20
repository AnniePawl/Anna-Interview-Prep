# Return True array contains value 

def check(seq, elem):
  return elem in seq

print(check([66,54,67], 66)) # True 
print(check([12,13,14], 90)) # False
print(check([21,34,56], 34)) # True 