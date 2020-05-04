# Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b. Note: a and b are not ordered. 

def get_sum(a,b):
  if a == b:
    return a 
  sum = 0 
  for n in range(min(a,b), max(a,b)+1):
    sum += n
  return  sum

  

print(get_sum(0,1)) # 1
print(get_sum(0,-1)) # -1
print(get_sum(2,2)) # 2
print(get_sum(-1,2)) # 2