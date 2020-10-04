# Given two coordinates, return YES if queen can move from start to end position 


def queen_move(a,b,c,d):
  if a == c or b == d:
    return "YES"
  elif abs(a-c) == abs(b-d):
    return "YES"
  else:
    return "NO"


print(queen_move(1,1,2,2)) # YES
print(queen_move(1,1,2,3)) # NO
