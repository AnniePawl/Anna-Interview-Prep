# Given 3 ints, return 3 if all are the same, 2 if 1 are the same, or 0 if all differet

def same_nums(a,b,c):
  if a == b == c:
    return 3 
  
  

print(same_nums(1,2,3)) # 1
print(same_nums(3,3,3)) # 3
print(same_nums(3,2,3)) # 2