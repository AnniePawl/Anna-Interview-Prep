# Given an int, print all squares less than or equal to in in ascending order 

def squares(n):
  num = 1 
  squares = []
  while num ** 2 <= n:
    squares.append(num**2)
    num += 1
  return squares
  
print(squares(50)) # 1 4 9 16 25 36 49