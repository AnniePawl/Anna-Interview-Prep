# Print ladder of n steps w/o spaces 

def ladder(n):
  for row in range(1, n+1):
    for column in range(1, row+1):
      print(column, end = ' ')
    # print(" ")



print(ladder(3))
# 1
# 12
# 123

def ladder2(n):
  for i in range(1, n +1):
    for j in range(1, i + 1):
      print(j, end=" ")
    print(" ")

print(ladder2(5))