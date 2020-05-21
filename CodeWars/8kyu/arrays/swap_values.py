# Swap the input values 

def swap(args):
  return [args[1], args[0]]

def swap2(args):
  return args[::-1]

def swap2(args):
  args[0], args[1] = args[1], args[0]
  returns args
  
print(swap([1,5])) # [5,1]
print(swap([2,3])) # [3,2]

print(swap2([1,5])) # [5,1]
print(swap2([2,3])) # [3,2]