# Given two coordinates, return YES if bishop can move from start to end. Otherwise return NO

def bishop_move(a,b,c,d):
  if abs(a-c) == abs(b-d):
    return "YES"
  else:
    return "NO"

print(bishop_move(4,4,5,5)) # YES
print(bishop_move(5,3,4,3)) # NO