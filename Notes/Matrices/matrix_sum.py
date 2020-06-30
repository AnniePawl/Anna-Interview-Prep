# Given a matrix, calculate the sum 

matrix = [[1,2,3],[4,5,6],[7,8,9]] # sum = 45 

sum = 0 
for row in matrix:
  for elem in row:
    sum += elem
print(sum)