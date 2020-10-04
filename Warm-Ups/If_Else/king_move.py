# Given a starting and ending position, return YES if king can move to end position and NO otherwise 


def king_move(a,b,c,d):
  if abs(a-c) == 1 and abs(b-d) == 1:
    return "YES"
  else:
    return 'NO'

print(king_move(4,4,5,5)) # YES
print(king_move(5,4,6,8)) # NO