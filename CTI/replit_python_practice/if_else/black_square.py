# Given square on chessboard (a,b), if square is black, print YES, else print NO 

def black_square(a,b):
  if a % 2 != 0  and b % 2 != 0:
    return "YES"
  elif a % 2 == 0 and b % 2 == 0:
    return "YES"
  else:
    return "NO"
  

print(black_square(1,1)) # YES
print(black_square(1,2)) # NO
print(black_square(2,4)) # YES
print(black_square(3,6)) # NO


# CTI Solution:
x1 = int(input())
y1 = int(input())

if (x1 + y1) % 2 == 0:
  print('YES')
else:
  print('NO')