# Given placement of 8 queens, print YES they threathen eachother, otherwise NO 


def eight_queens(coordinates):
  columns = []
  rows = []
  for num in coordinates[::2]:
    columns.append(num)
  for num in coordinates[1::2]:
    rows.append(num)

  # Check if in same row or column 
  for num in columns:
    if columns.count(num) > 1:
      return "YES"
  for num in rows:
    if rows.count(num) > 1:
      return "YES"
 

  # Check in in same diagonal 
  index1 = 0 
  index2 = 1
  if abs(columns[index1]- columns[index1]) == abs(rows[index2]-rows[index2]):
    return "YES"
  else:
    index1 += 1
    index2 +=1

  # return "NO"
    
  



print(eight_queens([1,5,2,3,3,1,4,7,5,2,6,8,7,6,8,4])) # NO
print(eight_queens([1,5,1,3,3,1,4,7,5,3,6,8,7,6,8,4])) # YES
print(eight_queens([1,8,2,7,3,6,4,5,5,4,6,3,7,2,8,1])) # YES
