# Check if value is in array w/o using loops 

def no_loops(a,x):
  return x in a

def no_loops2(a,x):
  return a.count(x) > 0 

print(no_loops([12,22,32,42,52], 32)) # True
print(no_loops(["my", "name", "is"], "doob")) # False


print(no_loops2([12,22,32,42,52], 32)) # True
print(no_loops2(["my", "name", "is"], "doob")) # False
