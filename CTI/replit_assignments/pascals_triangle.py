# given numRows, generate numRows of Pascal's triangle 
# To generaate A[C] in row R, sum up A[C] and A[C-1] from previous row R-1
# Since it's an interative problem, use a for loop

def pascals_triangle(numRows):
  triangle = [[] for i in range(numRows)]
  for row in range(numRows):
    for column in range(row + 1):
      if column < row:
        if column == 0:
          triangle[row].append(1)
        else:
          triangle[row].append(triangle[row-1][column]+triangle[row-1][column-1])
      elif (row == column):
        triangle[row].append(1)
  return triangle

print(pascals_triangle(5))
# [
#      [1],
#      [1,1],
#      [1,2,1],
#      [1,3,3,1],
#      [1,4,6,4,1]
# ]


# Another Solution 
def pascal_triangle(numRows):
  current_row=[1]
  triangle = [current_row]
  for i in range(1,numRows):
      next_row = []
      next_row.append(current_row[0])
      for i in range(len(current_row)-1):
          next_row.append(current_row[i]+current_row[i+1])
      next_row.append(current_row[-1])
      current_row=next_row
      triangle.append(next_row)
  return triangle

print(pascal_triangle(5))