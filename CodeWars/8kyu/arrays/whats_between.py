# Take in 2 integers, return array of all integers between parameters, including them 

def between(a,b):
  return list(range(a,b+1))

print(between(1,4)) # [1,2,3,4]