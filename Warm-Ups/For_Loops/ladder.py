# Given an int, print ladder up to int without spaces 


def ladder(n):
  for row in range(1,n+1):
    for column in range(1,row+1):
      print(column, end = '')
    print()


print(ladder(3))
# 1
# 12
# 123