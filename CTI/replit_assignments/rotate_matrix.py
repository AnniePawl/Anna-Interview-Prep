# Given NxN matrix, rotate it by 90 degrees (square)
# Perform operations in place using O(1) space 

def rotate_matrix(matrix):
  for row in range(len(matrix)):
    for col in range(len(matrix)):
      matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
  return matrix


# print(rotate_matrix([
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]))

#  [
#   [7, 4, 1]
#   [8, 5, 2]
#   [9, 6, 3]
# ]

# Visualize Transformations 

  [
  [1, 2, 3], [0,0] -> [0,2]
  [4, 5, 6],
  [7, 8, 9]
],

 [
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]




def rotate_matrix(matrix):
  for row in matrix:
    print(row)
  
  print("--before reverse--")
    
  for row in range(len(matrix)):
    for col in range(row,len(matrix)):
      print(row,col, " swaps with ", col, row)
      matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
  
  for row in matrix:
    print(row)
  print("--after--")
  for row in matrix:
    row.reverse()
    print(row)

rotate_matrix([
  [1, 2, 3,5],
  [4, 5, 6, 'f'],
  [7, 8, 9, 'b'],
  ['q', 'w', 'g', 'b']
])

"""
# flip

0,0 -> 0,2
2,0 -> 0,0

2,2 -> 2,0
0,2 -> 2,2

0,1 -> 1,2
2,1 -> 1,0

## swap
1,0 -> 0,1
1,1 -> 1,1
1,2 -> 2,1





"""