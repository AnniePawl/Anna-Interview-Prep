# https://pynative.com/print-pattern-python-examples/

# Print the following pattern 
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

for row in range(1,6):
  for column in range(1, row+1):
    print(column, end = ' ')
  print()

# Print the following pattern 
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 

for row in reversed(range(1, 6)):
  for column in range(1, row + 1):
    print(column, end = ' ')
  print()


# Print the following pattern
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

n = 5 
k = 5 
for i in range(0, n+1):
  for j in range(k-i, 0, -1):
    print(j, end = ' ')
  print()


# Print the following pattern 
# 5 
# 5 4
# 5 4 3  
# 5 4 3 2  
# 5 4 3 2 1






