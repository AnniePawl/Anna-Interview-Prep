# Given an int, print all squares where square is less than or equal to n in ascending order 

def squares(num):
  squares = []
  for number in range(1, num +1):
    square = number ** 2
    if square <= num:
      squares.append(square)
  return squares

print(squares(1))
print(squares(10)) # 1 4 9 
print(squares(50)) # 1 4 9 16 25 36 49

    
def squares2(num):
  i = 1 
  while i ** 2 <= num:
    print( i ** 2, end = " ")
    i += 1
  

print(squares2(10)) # 1 4 9 
print(squares2(50)) # 1 4 9 16 25 36 49


 

# Squares list comprehension 
def get_squares(num):
  return [x ** 2 for x in range(1, num +1)]



# print(get_squares(10)) # 1 4 9 
# print(get_squares(50)) # 1 4 9 16 25 36 49