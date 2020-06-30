# Given two numbers (rows & columns), create a matrix of that size filled with zeros 

def matrix_of_zeros(r,c):
  for row in range(r):
    for column in range(c):
      print([0*r][0* c], end = ' ')
    print()

def matrix_of_zeros2(r,c):
  matrix = [[0] * c for i in range(r)]
  return matrix

def matrix_of_zeros3(r,c):
  pass 


print(matrix_of_zeros(3,4))
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0 

print(matrix_of_zeros2(3,4))

print(matrix_of_zeros3(3,4))