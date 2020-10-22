# Produce an array with numbers 0-n-1

def arr(n=0):
  return [x for x in range(n)]

print(arr()) # []
print(arr(4)) # [0,1,2,3]