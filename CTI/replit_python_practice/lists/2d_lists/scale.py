# Given two integers - the number of rows m and columns n of m×n 2d list - and subsequent m rows of n integers, followed by one integer c. Multiply every element by c and print the result.

def scale_matrix(matrix, scale):
  matrix = [[column * scale for column in row] for row in matrix]
print(scale_matrix([[1,2,3], [4,5,6], [7,8,9]], 2))

# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# scale = 2 

m,n = input().split()
a = [[int(j) for j in input().split()] for i in range(int(m))]
c = int(input())
a = [[column * c for column in row] for row in a]
print(a)

# CTI Solution 
m, n = [int(s) for s in input().split()]
a = [[int(j) for j in input().split()] for i in range(m)]
c = int(input())
for i in range(m):
  for j in range(n):
    a[i][j] *= c
for line in a:
  print(*line)
