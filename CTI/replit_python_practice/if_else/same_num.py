# Given 3 ints, return 3 if all are the same, 2 if 1 are the same, or 0 if all different

def same_nums(a,b,c):
  if a == b == c:
    return 3 
  elif a == b or a == c or b == c:
    return 2
  else:
    return 0
  
  

print(same_nums(1,2,3)) # 0
print(same_nums(3,3,3)) # 3
print(same_nums(3,2,3)) # 2
