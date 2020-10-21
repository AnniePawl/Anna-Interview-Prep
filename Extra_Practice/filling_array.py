# Produce array with numbers 0 to n-1

def arr(n=0):
    return [x for x in range(n)]

print(arr(4)) # [0,1,2,3]
print(arr(0)) # []
print(arr()) # []
