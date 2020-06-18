# Print the following pattern 
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5


for num in range(1,11):
  print(str(num) * num)


for row in range(1, 6):
  for column in range(1, row +1):
    print(column, end = ' ') # puts space between each num 
  print("")
