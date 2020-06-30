
matrix = [[1,2,3], [4,5,6], [7,8,9]]
matrix2 = [[1,2,3,4], [5,6], [7,8,9]]


for i in range(len(matrix)):
  for j in range(len(matrix[i])):
    print(matrix[i][j], end= '  ')
  print()


for i in range(len(matrix2)):
  for j in range(len(matrix2[i])):
    print(matrix2[i][j], end= '  ')
  print()


for row in matrix:
  for element in row:
    print(element, end = ' ')
  print()

# Calculate matrix sum 
sum = 0 
for row in matrix:
  for element in row:
    sum += element 
print(sum)