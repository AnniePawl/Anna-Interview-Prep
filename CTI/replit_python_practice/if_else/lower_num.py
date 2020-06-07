# Return lower of 2 numbers 

def lower(a,b):
  return a if a<b else b 

print(lower(1,3)) # 1
print(lower(6,2)) # 2

# Return lowest of 3 numbers
def lowest(a,b,c):
 return min(a,b,c)

print(lowest(5,2,5)) # 2 