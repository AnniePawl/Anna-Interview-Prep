# Given an int, print all squares where square is less than or equal to n in ascending order 

def squares(num):
  squares = []
  for char in range(0, num):
    while char ** 2 <= num:
      squares.append(char ** 2)
  return squares

print(squares(10)) # 1 4 9 
print(squares(50)) # 1 4 9 16 25 36 49