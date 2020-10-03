# Given a square on a chessboard, print YES if it's Black and NO if its white  


def chess_square(a,b):
  if a % 2 != 0 and b % 2 != 0:
    return "YES"
  elif a % 2 == 0 and b % 2 == 0:
    return "YES"
  else:
    return "NO"

    
  

print(chess_square(1,1)) # YES
print(chess_square(4,1)) # NO
print(chess_square(3,5)) # YES